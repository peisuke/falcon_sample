# falcon_sample

This repository is sample to use falcon API. This API recevies binarized image data and sends image size.

# How to use

Start up API server.

```sh
$ docker build -t falcon_sample .
$ docker run -it -p 8000:8000 --rm falcon_sample
```

Send image to the server, and output image size.

```sh
$ python client.py
```
