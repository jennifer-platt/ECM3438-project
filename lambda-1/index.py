import http.client
import sys
import os
import boto3
import subprocess
import requests
from cdo import *

def handler(event, context):

    clientId = os.environ['CLIENT_ID']
    clientSecret = os.environ['CLIENT_SECRET']
    orderId = os.environ['ORDER_ID']
    targetBucket = os.environ['TARGET_BUCKET']

    s3_client = boto3.client('s3')

    # cdo = Cdo()

    headers = {
        'x-ibm-client-id': clientId,
        'x-ibm-client-secret': clientSecret,
        'accept': 'application/x-grib'
        }

    try: 
        r = requests.get('https://api-metoffice.apiconnect.ibmcloud.com/metoffice/production/1.0.0/orders/'+orderId+'/latest/ground_temperature_+00/data', headers=headers)
    
        print('Request status code: ' + str(r.status_code))

        gribFile = '/tmp/temp.grib2'
        ncFile = '/tmp/temp.nc'

        with open(gribFile, mode='wb') as localfile:     
            localfile.write(r.content)

        # gribToNcdf = subprocess.run(['cdo', '-f', 'nc', 'copy', gribFile, ncFile])

        cdo.copy(input=gribFile, output=ncFile, options='-f nc')

        # s3_client.upload_file('/'+covFile, targetBucket, covFile)

        # print('Upload to '+targetBucket+' complete')
    
    except Exception as e:
        return(e)

    