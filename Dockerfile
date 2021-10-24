# syntax=docker/dockerfile:1
FROM python:3.9-alpine
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
# Directory creation process
RUN mkdir /code
WORKDIR /code
COPY ./code/ /code

