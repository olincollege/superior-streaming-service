import urllib.request
import json
apiKey="KiPGkbzEgEKUwhVXB3WARAco0prVUiCdWSuPiTUb"


def fetchSourceData():

  #params to take in 
    #types:this is the type of accounts offered i.e sub,free,purchase
    #regions:this the region where this streaming services are found 
     #https://api.watchmode.com/v1/sources/?apiKey=KiPGkbzEgEKUwhVXB3WARAco0prVUiCdWSuPiTUb&regions=US
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

def fetchlistTitleData():
    movies_array=[]
    total_pages=57
    page=1
    while page<total_pages:
        with urllib.request.urlopen(f"https://api.watchmode.com/v1/list-titles/?apiKey={apiKey}&source_ids=203,387,372,159,26&page={page}") as url:
          data = json.loads(url.read().decode())
          print(page)
          movies_array+=data["titles"]
          # print(data["total_pages"])
          # writeIntoJson(data["titles"])
          page+=1
    return movies_array

def writeToFile():
    data=fetchlistTitleData()
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)











writeToFile()