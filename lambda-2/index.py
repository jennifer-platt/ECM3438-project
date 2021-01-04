import sys
import os
import boto3
import subprocess
import pycovjson.convert as convert
# from cdo import *

def handler(event, context):

    s3_client = boto3.client('s3')

    try: 
        ncFile = 'temp.nc'
        covFile = 'coverage.covjson'

        convert.main(ncFile, covFile, 't')

        return('Conversion complete')

        # s3_client.upload_file('/'+covFile, targetBucket, covFile)

        # print('Upload to '+targetBucket+' complete')
    
    except Exception as e:
        return(e)

    