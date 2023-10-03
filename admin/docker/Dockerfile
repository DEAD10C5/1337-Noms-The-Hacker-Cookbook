# syntax=docker/dockerfile:1

FROM python:3.12-slim-bullseye

LABEL org.opencontainers.image.authors="Franklin D <devsecfranklin@duck.com>"
LABEL org.opencontainers.image.source="https://github.com/DEAD10C5/1337-Noms-The-Hacker-Cookbook"
LABEL org.opencontainers.image.description="Ye Olde Hacker Cookbook"
LABEL org.opencontainers.image.licenses="CCC 1.0"

ENV DEBIAN_FRONTEND noninteractive
ADD . /app
WORKDIR /app

RUN \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367;\
    apt update; \
    apt install -y apt-utils;\
    apt -y autoremove;\
    apt install -y make git

# Python3 setup
RUN pip3 install -rrequirements.txt
