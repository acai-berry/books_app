FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./app/requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY ./app/ /app
