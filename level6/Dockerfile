# syntax=docker/dockerfile:1.4

FROM python:3.12.2-alpine3.18 AS builder
EXPOSE 8000
WORKDIR /targetserver
COPY ./app .
RUN apk update && \
    pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt
CMD gunicorn --bind 0.0.0.0:8000 --limit-request-line 7057 app:app