FROM python:3.13-slim
LABEL maintainer="lev2099@gmail.com"

ENV PYTHONNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .