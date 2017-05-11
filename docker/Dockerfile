FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get -y install --no-install-recommends \
    build-essential \
    python3-dev \
    python3-pip \
    python3-setuptools \
    git && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install \
    gunicorn \
    falcon \
    msgpack-python \
    falcon_multipart \
    pillow

RUN git clone https://github.com/peisuke/falcon_sample.git

WORKDIR /falcon_sample

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app"]
