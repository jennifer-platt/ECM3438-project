# Useful Docker commands

## Build docker image
`docker build -t container-name:tag .`

## Run docker image (in interactive mode)
`docker run -i -t container-name:tag`

## Login to AWS ECR container
`aws ecr get-login-password --region region | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.region.amazonaws.com`

## Push image to AWS ECR container
`docker push aws_account_id.dkr.ecr.us-east-1.amazonaws.com/hello-world:latest`

# Useful file conversion commands

## Convert GRIB2 file to NETCDF
`cdo -f nc copy first_file.grib2 second_file.nc`

## Read contents of NETCDF
`ncdump -h second_file.nc` or `pycovjson-viewer -v second_file.nc`

## Remove data variable from NETCDF
`ncwa -a variable_name second_file.nc third_file.nc`

## Convert NETCDF to coverageJSON
`pycovjson-convert -i third-file.nc -v variable_name`

# Useful AWS CLI commands

## Upload local file to S3 bucket
`aws s3 cp local-file s3://bucket-name`

## Configure AWS CLI
`aws configure`
