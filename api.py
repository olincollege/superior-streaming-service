import urllib.request
import json
apiKey="KiPGkbzEgEKUwhVXB3WARAco0prVUiCdWSuPiTUb"


def fetchSourceData():
    with urllib.request.urlopen(f"https://api.watchmode.com/v1/sources/?apiKey={apiKey}") as url:
      data = json.loads(url.read().decode())
      print(data)

def fetchRegionData():
    with urllib.request.urlopen(f"https://api.watchmode.com/v1/regions/?apiKey={apiKey}") as url:
      data = json.loads(url.read().decode())
      print(data)

def fetchNetworkData():
    with urllib.request.urlopen(f"https://api.watchmode.com/v1/networks/?apiKey={apiKey}") as url:
      data = json.loads(url.read().decode())
      print(data)   

def fetchGenreData():
    with urllib.request.urlopen(f"https://api.watchmode.com/v1/genres/?apiKey={apiKey}") as url:
      data = json.loads(url.read().decode())
      print(data) 

def fetchTitleData():
    with urllib.request.urlopen(f"https://api.watchmode.com/v1/title/345534/details/?apiKey={apiKey}") as url:
      data = json.loads(url.read().decode())
      print(data)















fetchSourceData()