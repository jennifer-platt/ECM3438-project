FROM public.ecr.aws/lambda/python:3.8

RUN pip install \
    requests \
    numpy \
    xarray \
    cdo --target=/opt \
    boto3 \
    netcdf4 \
    scipy

COPY index.py   ./
COPY converter   ./

CMD ["index.handler"]