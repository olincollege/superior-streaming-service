import urllib.request
import json
apiKey="SI4GiZabAskTGu45hy9LUzyQThhVeJzMor9iY3rD"
apiKey2='VPj1VSW4gltUJXs40u0o7kdozDToKqYWco0a7zNc'
apiKey3='YsD9TJSwufHmkcTOKqZ7SAPhdLirB8kRldcJ9pNB'
testApi1='ksDAw94LqRdMIpZJGAXcwlGcIO5Ritn4ZQz5Xi7c'
testApi2="TWocNuvi7WVBGGULh1TdThsT8c9oU2AGHCtPN7O8"
testApi3="FF6tlX26yEjdRPKcz4Ki4UY025GOWsIQzrq0OV5C"
testApi4="9JeALxiKnHzjSR5iWgZCQjKGLpBl8uEOVPK8a0Pi"
testApi5="vaXqIU2y3AB0GSwhZQRgLYYhUsHQPjEO4AvQnFHt"
testApi6="rrFdXashTiwZVMCASk6aAgmMFjnb7JyXmcd9yglu"
testApi7="oWBeZ4Up3ESsGPZRn9wmlISCndVW1G2ZV7nbXakx"



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
  #  current_api_key=apiKey
  #  if  count % 2 == 0:
  #    current_api_key=apiKey
  #  elif count % 3:
  #    current_api_key=apiKey2
  #  else:
  #    current_api_key=apiKey3

   with urllib.request.urlopen(f"https://api.watchmode.com/v1/title/{id}/details/?apiKey={testApi4}") as url:
      data = json.loads(url.read().decode())
      print(data)
      if data:
         return data
      return

def fetchlistTitleData():
    movies_array=[]
    total_pages=34
    page=1
    while page<=total_pages:
        with urllib.request.urlopen(f"https://api.watchmode.com/v1/list-titles/?apiKey={apiKey3}&source_ids=26&page={page}") as url:
          data = json.loads(url.read().decode())
          print(page)
          movies_array+=data["titles"]
          # print(data["total_pages"])
          # writeIntoJson(data["titles"])
          page+=1
    return movies_array


def writeToFile():
    data=fetchlistTitleData()
    with open('amazon.txt', 'w') as outfile:
        json.dump(data, outfile)

def fetchTitleDetails(srcfile,source):
    with open(srcfile) as json_file:
     data = json.load(json_file)
     titles=[]
     count=0
     for i in data:
       if count <=100:
        print(count)
        title=fetchTitleData(i['id'],count)
        title['source']= source
        titles.append(title)
        count+=1
       else:
         break 
     return titles
def saveTitleData():
    data=fetchTitleDetails("amazon.txt","Amazon Prime")
    with open('amazontitles.txt', 'w') as outfile:
        json.dump(data, outfile)

def analyzeTitleData():
  with open('crackletitle.txt') as json_file:
     data = json.load(json_file)
     for i in data:
         if i['genres'] != None:
            print(i['genres'][:1])
       






saveTitleData()