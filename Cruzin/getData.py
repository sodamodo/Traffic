# import models

import requests

r = requests.get('http://207.251.86.229/nyc-links-cams/LinkSpeedQuery.txt')

text = r.text

format = text.split('\n')
line = format[1].split('\t')

print line



