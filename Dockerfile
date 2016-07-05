FROM python:2.7.11-alpine

ADD /src/requirements.txt /opt/app/requirements.txt

RUN apk update
RUN apk add libffi-dev
RUN apk add python-dev
RUN apk add g++ make

WORKDIR /opt/app
RUN pip install -r /opt/app/requirements.txt
