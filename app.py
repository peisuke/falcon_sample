import os
import io
import falcon
import msgpack
from falcon_multipart.middleware import MultipartMiddleware
from PIL import Image
import json

class Resource(object):
  def on_post(self, req, resp):
    body = req.stream.read()
    image_binary = req.get_param('file').file.read()
    stream = io.BytesIO(bytearray(image_binary))
    picture = Image.open(stream)
    resp.status = falcon.HTTP_201
    
    ret = {
      'width': picture.size[0],
      'height': picture.size[1]
    }
    ret = json.dumps(ret)
    resp.body = ret

api = application = falcon.API(middleware=[MultipartMiddleware()])

images = Resource()
api.add_route('/images', images)
