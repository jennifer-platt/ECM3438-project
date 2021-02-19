# import http.client
import os
import boto3
from botocore.exceptions import ClientError
import subprocess
import requests
# import pycovjson.convert as convert

def converter(event, context):

    # clientId = os.environ['CLIENT_ID']
    # clientSecret = os.environ['CLIENT_SECRET']
    # orderId = os.environ['ORDER_ID']
    # targetBucket = os.environ['TARGET_BUCKET']

    # s3_client = boto3.client('s3')
    
    # headers = {
    #     'x-ibm-client-id': clientId,
    #     'x-ibm-client-secret': clientSecret,
    #     'accept': 'application/x-grib'
    #     }
    
    layers = ["ground_temperature_+00", "ground_total-precipitation-rate_+00"]

    for layer in layers:
        print(layer)
        # try: 
        #     r = requests.get('https://api-metoffice.apiconnect.ibmcloud.com/metoffice/production/1.0.0/orders/'+orderId+'/latest/'+layer+'/data', headers=headers)
        
        #     print('Request status code: ' + str(r.status_code))

        #     gribFile = 'temp.grib2' if layer == "ground_temperature_+00" else 'precip.grib2'
        #     ncFile = 'temp.nc' if layer == "ground_temperature_+00" else 'precip.nc'
        #     covFile = 'temp.covjson' if layer == "ground_temperature_+00" else 'precip.covjson'

        #     with open(gribFile, mode='wb') as localfile:     
        #         localfile.write(r.content)         

        #     if layer == "ground_temperature_+00":
        #         ncFile2 = 'temp2.nc'
        #         ncFile3 = 'temp3.nc'

        #         gribToNcdf = subprocess.run(['cdo', '-f', 'nc', 'copy', gribFile, ncFile3])
        #         convertKToC = subprocess.run(['cdo', 'subc,273.15', ncFile3, ncFile2]) 
        #         renameTempVariable = subprocess.run(['cdo', 'setattribute,t@units="degC"', ncFile2, ncFile]) 
        #     else:
        #         gribToNcdf = subprocess.run(['cdo', '-f', 'nc', 'copy', gribFile, ncFile])

        #     variable = 't' if layer == "ground_temperature_+00" else 'tprate'

        #     convert.main(ncFile, covFile, variable)

        #     print('Conversion complete')

        #     s3_client.upload_file('/'+covFile, targetBucket, covFile)

        #     print('Upload to '+targetBucket+' complete')
        
        # except Exception as e:
        #     print(e)
