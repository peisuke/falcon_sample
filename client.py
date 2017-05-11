import requests
import os
import json
from PIL import Image 

filepath = os.path.join('./', 'test.jpg')
image = open(filepath, 'rb')

url = "http://127.0.0.1:8000/images"
s = requests.session()
r = s.post(url, files={'file': image})

ret = json.loads(r.content.decode('utf-8'))

print('STATUS: {0}'.format(r.status_code))
print('width:{0}, height:{1}'.format(ret['width'], ret['height']))
