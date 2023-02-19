# syntax=docker/dockerfile:1
FROM python:3.10-slim-buster

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . .

# CMD ["python3", "-m", "flask", "run"]
CMD ["python", "app.py"]
# ENTRYPOINT ["gunicorn", "-b", ":8080"]
# CMD [ "app:create_app()" ]