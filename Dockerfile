FROM python:3.7-alpine
MAINTAINER safariko

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /calculator
WORKDIR /calculator
COPY ./calculator /calculator

RUN adduser -D user
USER user
