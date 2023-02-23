# syntax=docker/dockerfile:1
FROM python:3.10-slim-buster

WORKDIR /web

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /web

RUN pip install -r requirements.txt

COPY . .

CMD ["./entrypoint.sh"]