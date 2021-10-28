FROM python:3.9-slim-buster

RUN apt-get update -yqq \
    && apt-get install -yqq git\
    && apt-get -y clean && rm -rf /var/lib/apt/lists/*

COPY ./run.py /run.py

CMD ["python", "/run.py"]
