FROM python:3.10.4 AS base

RUN apt-get update && apt-get upgrade -y

COPY . /src/
WORKDIR /src
ENTRYPOINT ["./main"]
