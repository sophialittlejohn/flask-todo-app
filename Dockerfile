FROM continuumio/miniconda:latest

RUN apt-get update && apt-get install -y wget bzip2

RUN mkdir -p /app | \
    mkdir -p /run

COPY ./app/requirements.yml /app/requirements.yml

RUN /opt/conda/bin/conda env create -f /app/requirements.yml

ENV PATH /opt/conda/envs/app/bin:$PATH

COPY ./app /app

COPY ./scripts/* /app/scripts/
RUN chmod +x /app/scripts/*

WORKDIR /app