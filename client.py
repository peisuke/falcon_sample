import argparse
import requests
import os
import json
from PIL import Image 

parser = argparse.ArgumentParser(description='FALCON API Client')
parser.add_argument('--data', '-d', type=str, required=True, help='Path to target image')
parser.add_argument('--ip', '-i', default='127.0.0.1', help='ip address to server')
parser.add_argument('--port', '-p', default='8000', help='port')
args = parser.parse_args()

image = open(args.data, 'rb')

url = "http://%s:%s/images" % (args.ip, args.port)
s = requests.session()
r = s.post(url, files={'file': image})

ret = json.loads(r.content.decode('utf-8'))

print('STATUS: {0}'.format(r.status_code))
print('width:{0}, height:{1}'.format(ret['width'], ret['height']))
