# syntax=docker/dockerfile:1
FROM python:3.10-slim-buster

WORKDIR /web

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
COPY requirements.txt /web
RUN pip install -r requirements.txt

COPY . /web/

CMD ["/web/entrypoint.sh"]