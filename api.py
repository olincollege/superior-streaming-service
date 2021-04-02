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



def fetch_source_data():

  #params to take in 
    #types:this is the type of accounts offered i.e sub,free,purchase
    #regions:this the region where this streaming services are found 
     #https://api.watchmode.com/v1/sources/?apiKey=KiPGkbzEgEKUwhVXB3WARAco0prVUiCdWSuPiTUb&regions=US
    with urllib.request.urlopen(f"https://api.watchmode.com/v1/sources/?apiKey={apiKey}") as url:
      data = json.loads(url.read().decode())
      print(data)

def fetch_region_data():
    with urllib.request.urlopen(f"https://api.watchmode.com/v1/regions/?apiKey={apiKey}") as url:
      data = json.loads(url.read().decode())
      print(data)

def fetch_network_data():
    with urllib.request.urlopen(f"https://api.watchmode.com/v1/networks/?apiKey={apiKey}") as url:
      data = json.loads(url.read().decode())
      print(data)   

def fetch_genre_data():
    with urllib.request.urlopen(f"https://api.watchmode.com/v1/genres/?apiKey={apiKey}") as url:
      data = json.loads(url.read().decode())
      print(data) 

def fetch_title_data(id,count):
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

def fetch_list_title_data():
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


def write_to_file():
    data=fetch_list_title_data()
    with open('amazon.txt', 'w') as outfile:
        json.dump(data, outfile)

def fetch_title_details(srcfile,source):
    with open(srcfile) as json_file:
     data = json.load(json_file)
     titles=[]
     count=0
     for i in data:
       if count <=100:
        print(count)
        title=fetch_title_data(i['id'],count)
        title['source']= source
        titles.append(title)
        count+=1
       else:
         break 
     return titles

def save_title_data():
    data=fetch_title_details("amazon.txt","Amazon Prime")
    with open('amazontitles.txt', 'w') as outfile:
        json.dump(data, outfile)

def analyze_title_data():
  with open('crackletitle.txt') as json_file:
     data = json.load(json_file)
     for i in data:
         if i['genres'] != None:
            print(i['genres'][:1])
       


#Plotting functions

#Merges all 5 individual files
def merge_files(file1, file2, file3, file4, file5, combined_file):
#I feel like theres a nicer way to have an unspecified number of args
#but this will do for now
  """
  Merges the data from 5 files into 1. This is useful for analyzing all of the
  data in a further function.

  Args:
  file1, file2, file3, file4, file5: all are strings representing the names of
  files (including the extension) that are to be combined.
  
  combined_file: a string representing the name of the file to be created

  Returns:
  Nothing, but creates a file named
  """
  filenames = [file1, file2, file3, file4, file5]
  with open(combined_file, 'w') as outfile:
    
    # Iterate through list
    for names in filenames:
    
        # Open each file in read mode
        with open(names) as infile:
          outfile.write(infile.read())

        outfile.write("\n")
  pass

def get_genre(genre, list=False):
  """
  Decodes genres and returns all movies of the inputted genre

  Args: 
  genre: a string containing the name of the genre

  list: an optional argument in case the user wants to see the list of genres
  that are available. It is a boolean. If list = True, then the list of genres
  will be returned; otherwise, it will not be returned.

  Returns:
  A list of dictionaries of all of the movies across 5 streaming services that fit
  within a genre
  """
  #return list of valid genres
  #decoding the genre
  with open("genre.txt") as json_file:
    genre_data = json.load(json_file)
    specific_genre = [item for item in genre_data if item["name"] == genre]
    genre_number = specific_genre[0]["id"]

  #get all movies with genre id "genre_number" 
  with open("movie_details_list.txt") as json_file:
    #CREATE MOVIE
    movies_list = json.load(json_file)

#getting list of movies
pass


#saveTitleData()

merge_files("disneyplustitles.txt", "amazontitles.txt", "netflixtitles.txt", "hbomaxtitles.txt", "hulutitles.txt")