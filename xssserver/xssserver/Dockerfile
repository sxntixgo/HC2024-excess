# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.12.2-alpine3.18 AS builder
EXPOSE 8000
WORKDIR /xssserver 
COPY requirements.txt /xssserver/requirements.txt
RUN apk update && apk add git curl tar firefox && \
    pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt && \
    pip3 install --no-cache-dir git+https://github.com/math-a3k/django-bootstrap-v5.git#egg=django-bootstrap-v5 && \
    curl -L https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux64.tar.gz | tar xz -C /usr/local/bin
COPY . /xssserver