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
$ python client.py -d ./test.jpg -i 127.0.0.1 -p 8000
```

The expected output is shown as below.

```sh
STATUS: 200
width:512, height:384
```
