FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt ./

RUN python3 -m pip install --upgrade pip \
    && pip install -r requirements.txt --no-cache-dir \
    && rm requirements.txt

COPY . /