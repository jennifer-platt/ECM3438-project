FROM debian:buster-slim

LABEL MAINTAINER="Anaconda, Inc"

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update -q && \
    apt-get install -q -y \
        ca-certificates \
        git \
        libglib2.0-0 \
        libsm6 \
        libxext6 \
        libxrender1 \
        wget \
        cron \
        awscli \
    && apt-get clean

ENV PATH /opt/conda/bin:$PATH

# Leave these args here to better use the Docker build cache
ARG CONDA_VERSION=py38_4.9.2
ARG CONDA_MD5=122c8c9beb51e124ab32a0fa6426c656

RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-${CONDA_VERSION}-Linux-x86_64.sh -O miniconda.sh && \
    echo "${CONDA_MD5}  miniconda.sh" > miniconda.md5 && \
    if ! md5sum --status -c miniconda.md5; then exit 1; fi && \
    mkdir -p /opt && \
    sh miniconda.sh -b -p /opt/conda && \
    rm miniconda.sh miniconda.md5 && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.js.map' -delete && \
    /opt/conda/bin/conda clean -afy

RUN conda install -c conda-forge requests && \
    conda install -c conda-forge python-cdo && \
    conda install -c conda-forge nco && \
    conda install -c conda-forge netcdf4 && \
    conda install -c conda-forge boto3 && \
    conda install -c conda-forge scipy && \
    conda install -c conda-forge numpy && \
    conda install -c conda-forge pandas && \
    conda install -c conda-forge xarray

COPY grib2ToCovjson.py   ./
COPY converter   ./
COPY crontab   /etc/cron.d/crontab

RUN crontab /etc/cron.d/crontab

CMD ["cron", "-f"]
