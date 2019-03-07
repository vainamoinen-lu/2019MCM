import urllib, json, requests

with urllib.request.urlopen("https://geo.fcc.gov/api/census/area?lat=42.3295&lon=-71.0826&format=json") as url:
    data = json.loads(url.read().decode())
    print(data)

# print(json.dumps(data, indent=4, sort_keys=True))
