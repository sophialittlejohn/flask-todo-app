FROM continuumio/miniconda:latest

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update && apt-get install -y wget bzip2

RUN mkdir -p /app | \
    mkdir -p /run

COPY ./app/requirements.yml /app/requirements.yml

RUN /opt/conda/bin/conda env create -f /app/requirements.yml

# this starts the environment
ENV PATH /opt/conda/envs/app/bin:$PATH

# this only get executed after the requirements have been done, so when you change something the container can start here rather than anywhere further up in the code
COPY ./app /app

COPY ./scripts/* /app/scripts/

# this makes the scrips executable
RUN chmod +x /app/scripts/*

WORKDIR /app