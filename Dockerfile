FROM python:3.7-alpine

COPY . /root

WORKDIR /root

RUN pip install flask gunicorn