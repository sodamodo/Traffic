# import models

import requests

r = requests.get('http://207.251.86.229/nyc-links-cams/LinkSpeedQuery.txt')

text = r.text

lines = text.split('\n')
linecoords = []
jsoncoords = []
joined = []
row = []
polylines = []
for i in range(1, len(lines)-1):
    row = lines[i].split('\t')
    coordstring = row[6].split(' ')
    linecoords.append(coordstring)


for n in linecoords:

    for i, z in enumerate(n):
        print z

    print n
    polylines.append(n)

for g in polylines:
    print g
# print polylines
# if '"' in z:
#             new = z.replace('"', "")
#             n[i] = new
#             print n[i]
#             print new

geoJson = """

{ "type": "FeatureCollection",
    "features": [
        #features go here
        ]
     }
"""

linestring = """

      { "type": "Feature",
        "geometry": {
          "type": "LineString",
          "coordinates": [
            [102.0, 0.0], [103.0, 1.0], [104.0, 0.0], [105.0, 1.0]
            ]
          },
        "properties": {
          "prop0": "value0",
          "prop1": 0.0
         }
        }
      } #feature closes here

          """
