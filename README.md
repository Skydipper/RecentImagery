# RecentImagery

Service for identifying satellite imagery tiles from Landsat and Sentinel-2.
You are able to search for a location, and time range, and set band visulisation parameters.

## Local docker

Run `./recentimagery.sh develop`

You can reach the service e.g. `localhost:4503/api/v1/recent-imagery?lat=-4.477615356445313&lon=39.38154876932644&start=2018-11-13&end=2019-02-12`

## Return a list of all intersecting satellite images

```python
import requests
url=f"http://api.skydipper.com/v1/recent-imagery"
params={"lat":28.399391877577933,
        "lon":-16.493425662438167,
        "start":"2019-11-1",
        "end":"2019-11-22",
        "bands":None}
r = requests.get(url,params=params)
print(r.json())
```

Returns a response like:

```json
{'data': {'id': None,
  'tiles': [{'attributes': {'bbox': {'geometry': {'coordinates': [[-15.92558389724579,
         28.925190549257714],
        [-15.92559671449868, 28.925191163600214],
        [-17.051433713664156, 28.91274387174152],
        [-17.051480391568088, 28.912706620290745],
        [-17.051531935518994, 28.912674682697084],
        [-17.05153490920881, 28.91265990682834],
        [-17.041910802259004, 28.41750963441286],
        [-17.032527124641494, 27.922327989157285],
        [-17.03248495569906, 27.922287141116684],
        [-17.032448913873885, 27.92224196307347],
        [-17.0324320643225, 27.922239418847433],
        [-15.917013741784361, 27.934185520299348],
        [-15.916967046088413, 27.93422235347645],
        [-15.91691560017191, 27.934253830965012],
        [-15.916912552853256, 27.93426863344697],
        [-15.921148642190191, 28.429707339526168],
        [-15.925493100926781, 28.92510186499591],
        [-15.925535317176289, 28.925143044864797],
        [-15.925571259256028, 28.925188529207674],
        [-15.92558389724579, 28.925190549257714]],
       'type': 'Polygon'}},
     'cloud_score': 57.3898,
     'date_time': '2019-11-17 11:52:21Z',
     'instrument': 'Sentinel-2A',
     'source': 'COPERNICUS/S2/20191117T115221_20191117T115220_T28RCS',
     'thumbnail_url': None,
     'tile_url': 'https://earthengine.googleapis.com/map/6c4d08f0e527f62e97d85a92c5c181bc/{z}/{x}/{y}?token=733263c1e4925c385702d2a18f2e39a6'
     }}]
  }
}
```

## Request tiles

You can use the response from the query to `/recent-imagery` to make a further request to `tiles` and `thumbs` endpoints.

```python
import requests
tiles_url = "http://api.skydipper.com/v1/recent-imagery/tiles"
body={"source_data": [{"source":'COPERNICUS/S2/20191107T115221_20191107T115221_T28RCS'},{"source":'LANDSAT/LC08/C01/T1_RT_TOA/LC08_207040_20191117'}],
            "min": None,
            "max": None,
            "opacity": 1.0,
            "bands": None}
r = requests.post(tiles_url, json=body)
print(r.json())
```

Which will result in a response such as:

```json
{'data': {'attributes': [{'source_id': 'COPERNICUS/S2/20191107T115221_20191107T115221_T28RCS',
    'tile_url': 'https://earthengine.googleapis.com/map/d58d121e0a14ccf17bb3fa08af87bb73/{z}/{x}/{y}?token=3fb09853e976ad45cfc4b3dc267f455a'},
   {'source_id': 'LANDSAT/LC08/C01/T1_RT_TOA/LC08_207040_20191117',
    'tile_url': 'https://earthengine.googleapis.com/map/277080042a8a4c5481346a3f341ed01a/{z}/{x}/{y}?token=613fe7ab781cde1fbca1e1b242c508aa'}],
  'id': None,
  'type': 'recentimages-tiles'}}
```

## Request thumbnails

```python
import requests
tiles_url = "http://api.skydipper.com/v1/recent-imagery/thumbs"
body={"source_data": [{"source":'COPERNICUS/S2/20191107T115221_20191107T115221_T28RCS'},{'source': 'COPERNICUS/S2/20191117T115221_20191117T115220_T28RCS'}, {"source":'LANDSAT/LC08/C01/T1_RT_TOA/LC08_207040_20191117'}],
            "min": None,
            "max": None,
            "opacity": 1.0,
            "bands": None}
r = requests.post(tiles_url, json=body)
print(r.json())
```

```json
{'data': {'attributes': [{'source': 'COPERNICUS/S2/20191107T115221_20191107T115221_T28RCS',
    'thumbnail_url': 'https://earthengine.googleapis.com/api/thumb?thumbid=ba7e8eb6d9606ad6191402148fc2e4dd&token=d732ad356760313627096ed9888944f4'},
   {'source': 'COPERNICUS/S2/20191117T115221_20191117T115220_T28RCS',
    'thumbnail_url': 'https://earthengine.googleapis.com/api/thumb?thumbid=caa55e2a982081b793c99dc95a7ca3d5&token=943827c8075eb9b3960bf95ee304b57a'},
   {'source': 'LANDSAT/LC08/C01/T1_RT_TOA/LC08_207040_20191117',
    'thumbnail_url': 'https://earthengine.googleapis.com/api/thumb?thumbid=8af65bde5696bd2189a225a7dff5d346&token=6087176665a1bbbe72604b810f72f308'}],
  'id': None,
  'type': 'recentimages-thumbs'}}
```