FROM python:3.7-alpine
LABEL "version" "1.0"
MAINTAINER "Apisod.com(awes0m)"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY . /app /app/

RUN adduser -D goduser
USER goduser


