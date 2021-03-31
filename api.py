import urllib.request
import json
apiKey="SI4GiZabAskTGu45hy9LUzyQThhVeJzMor9iY3rD"
apiKey2='VPj1VSW4gltUJXs40u0o7kdozDToKqYWco0a7zNc'
apiKey3='YsD9TJSwufHmkcTOKqZ7SAPhdLirB8kRldcJ9pNB'


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

def fetchTitleData(id,count):
   current_api_key=apiKey
   if  count % 2 == 0:
     current_api_key=apiKey
   elif count % 3:
     current_api_key=apiKey2
   else:
     current_api_key=apiKey3

   with urllib.request.urlopen(f"https://api.watchmode.com/v1/title/{id}/details/?apiKey={current_api_key}") as url:
      data = json.loads(url.read().decode())
      print(data)
      if data:
         return data
      return

def fetchlistTitleData():
    movies_array=[]
    total_pages=3
    page=1
    while page<=total_pages:
        with urllib.request.urlopen(f"https://api.watchmode.com/v1/list-titles/?apiKey={apiKey}&source_ids=77&page={page}") as url:
          data = json.loads(url.read().decode())
          print(page)
          movies_array+=data["titles"]
          # print(data["total_pages"])
          # writeIntoJson(data["titles"])
          page+=1
    return movies_array


def writeToFile():
    data=fetchlistTitleData()
    with open('crackle.txt', 'w') as outfile:
        json.dump(data, outfile)

def fetchTitleDetails():
    with open('crackle.txt') as json_file:
     data = json.load(json_file)
     titles=[]
     count=0
     for i in data:
       print(count)
       title=fetchTitleData(i['id'],count)
       titles.append(title)
       count+=1
     return titles
def saveTitleData():
    data=fetchTitleDetails()
    with open('crackletitle.txt', 'w') as outfile:
        json.dump(data, outfile)







saveTitleData()