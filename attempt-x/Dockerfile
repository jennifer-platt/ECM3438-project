ARG FUNCTION_DIR="/home/"

FROM python:3.8-slim-buster
ARG FUNCTION_DIR
RUN mkdir -p ${FUNCTION_DIR}
COPY index.py ${FUNCTION_DIR}

LABEL MAINTAINER="Anaconda, Inc"

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
# ENV CONDA_PKGS_DIRS=/usr/local/lib/python3.8/site-packages

RUN apt-get update -q && \
    apt-get install -q -y \
        ca-certificates \
        cron \
        git \
        libglib2.0-0 \
        libsm6 \
        libxext6 \
        libxrender1 \
        wget \
        g++ \
        make \
        cmake \
        unzip \
        libcurl4-openssl-dev \
    && apt-get clean

ENV PATH /opt/conda/bin:$PATH

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

RUN conda install -c conda-forge boto3 mock nco netcdf4 numpy pandas python-cdo scipy requests xarray

RUN /usr/local/bin/python3 -m pip install awslambdaric

WORKDIR ${FUNCTION_DIR}

ENTRYPOINT [ "/usr/local/bin/python3", "-m", "awslambdaric" ]
CMD [ "index.converter" ]
