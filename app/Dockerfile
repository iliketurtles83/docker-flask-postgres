# syntax=docker/dockerfile:1
FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app/

CMD ["python", "app.py"]
# ENTRYPOINT ["gunicorn", "-b", ":8080"]
# CMD [ "app.app:create_app()" ]