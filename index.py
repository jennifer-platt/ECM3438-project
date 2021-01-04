import http.client
import sys
import os
import boto3
import subprocess
import requests
import pycovjson.convert as convert
from cdo import *

def handler(event, context):

    clientId = 'a3663165-a786-4c64-a929-5f16fe5cf7bb'
    clientSecret = 'N2fO6vL4qD2xY5rB8aW7lR4dK3gW1uE2fW6mL0cV7mG2xW5jJ3'
    orderId = 'o124935823665'
    # targetBucket = os.environ['TARGET_BUCKET']

    s3_client = boto3.client('s3')

    # cdo = Cdo()
    
    headers = {
        'x-ibm-client-id': clientId,
        'x-ibm-client-secret': clientSecret,
        'accept': 'application/x-grib'
        }
    
    layers = ["ground_temperature_+00"]

    for layer in layers:
        try: 
            r = requests.get('https://api-metoffice.apiconnect.ibmcloud.com/metoffice/production/1.0.0/orders/'+orderId+'/latest/'+layer+'/data', headers=headers)
        
            print('Request status code: ' + str(r.status_code))

            gribFile = 'temp.grib2'
            ncFile = 'temp.nc'
            ncFile2 = 'temp2.nc'
            covFile = 'coverage.covjson'

            with open(gribFile, mode='wb') as localfile:     
                localfile.write(r.content)

            gribToNcdf = subprocess.run(['cdo', '-f', 'nc', 'copy', gribFile, ncFile2])

            if layer == "ground_temperature_+00":
                subprocess.run(['cdo', 'subc,273.15', ncFile2, ncFile]) 

            # cdo.copy(input=gribFile, output=ncFile, options='-f nc')

            convert.main(ncFile, covFile, 't')

            return('Conversion complete')

            # s3_client.upload_file('/'+covFile, targetBucket, covFile)

            # print('Upload to '+targetBucket+' complete')
        
        except Exception as e:
            return(e)

    