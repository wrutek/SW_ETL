FROM python:3.10.4 AS base

RUN apt-get update && apt-get upgrade -y

COPY . /src/
RUN pip install -r /src/requirements.txt

# this stage is meant for more "productish" use
FROM base AS main
WORKDIR /src
ENTRYPOINT ["./main.py"]

FROM base AS development
RUN pip install -r /src/requirements-dev.txt
WORKDIR /src
CMD ["./main.py", "fetch-characters"]
