import urllib.request
import json
import statistics
import numpy as np
import matplotlib.pyplot as plt
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




def fetch_title_data(id):
    """
    This function takes in an id of a movie and sends a request to the watchmode api to get the details of the movie.
    The API response is a dictionary with all the details of the said movie
    Args:
    id:this is the id of the movie
    Returns:
    The function returns a dictionary with all the relevant details of a movie
    
    """
    with urllib.request.urlopen(f"https://api.watchmode.com/v1/title/{id}/details/?apiKey={testApi4}") as url:
        data = json.loads(url.read().decode())
        print(data)
        if data:
          return data
        return

def fetch_list_title_data(source_id):
    """
    
    This function takes in a source id as a parameter and  sends a request to the watchmode api to get a list of all the movies from a certain source(Netflix,HBO).
    Since the watchmode API returns data in pages, the function iterates through all the pages untill it has gotten all the data from that particular source.

    Args:
    source_id:this is the id of a particular source.For example, Netflix source id is 243

    Returns:
    The function returns a list of all the movies that exist in that particular source

    """
    movies_array=[]
    total_pages=34
    page=1
    while page<=total_pages:
        with urllib.request.urlopen(f"https://api.watchmode.com/v1/list-titles/?apiKey={apiKey3}&source_ids={source_id}&page={page}") as url:
          data = json.loads(url.read().decode())
          print(page)
          movies_array+=data["titles"]
          page+=1
    return movies_array


def write_to_file():
    """

    This function writes all the movies from a specific source into one file.Once the `fetch_list_title_data` gets information from the watchmode API,
    this function then writes that data into a file

    """
    data=fetch_list_title_data("243")
    with open('amazon.txt', 'w') as outfile:
        json.dump(data, outfile)

def fetch_title_details(srcfile,source):
    """

    This function utilises `fetch_title_data` to fetch data from the watchmode api, it then iterates through the list of dictionaries and 
    appends the source attribute to each dictionary.

    Args:
      srcfile:This is the source fille to get data on all the movie titles
      source:This is the name of the source i.e Netflix

    Returns:
    The function returns all the titles of movies with the source they are from appended

    """ 
    with open(srcfile) as json_file:
     data = json.load(json_file)
     titles=[]
     count=0
     for i in data:
       if count <=100:
        title=fetch_title_data(i['id'],count)
        title['source']= source
        titles.append(title)
        count+=1
       else:
         break 
     return titles

def save_title_data():
    """

    This function writes all the movies titles from a specific source into one file.Once the `fetch_title_details` gets information from the watchmode API,
    this function then writes that data into a file
    
    """
    data=fetch_title_details("amazon.txt","Amazon Prime")
    with open('amazontitles.txt', 'w') as outfile:
        json.dump(data, outfile)


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

def decode_genre(genre):
  """
  Decodes genres by turning the name of the genre into an encoded number

  Args: 
  genre: a string containing the name of the genre

  Returns:
  A list of dictionaries of all of the movies across 5 streaming services that fit
  within a genre
  """
  #decoding the genre
  with open("genre.txt") as json_file:
    genre_data = json.load(json_file)
    specific_genre = [item for item in genre_data if item["name"] == genre]
    genre_number = specific_genre[0]["id"]
  return genre_number


#might not need this
def get_movies(genre):

  """

  Decodes genres and returns all movies of the inputted genre

  Args: 
  genre: a string containing the name of the genre

  Returns:
  A list of dictionaries of all of the movies across 5 streaming services that fit
  within a genre.
  """
  #get all movies with genre id "genre_number" 
  genre_number = decode_genre(genre)
  genre_movies=[]
  with open("movie_details_list.txt") as json_file:
    movies_list = json.load(json_file)
    # print(movies_list)
    for item in movies_list:
        # print(item['genres'])
      if item['genres']!= None:
        if genre_number in item['genres']:
           genre_movies.append(item)
    if genre_movies == []:
      print(f"No {genre} movies found")
    else:
      return genre_movies

def get_genre_ratings(genre, source):
  """
  Gets the average user rating of a movies in a genre within a specified source.

  Args:
  genre: string; the genre we are looking to explore the ratings for.
  source: string; the specific source within which we are looking to get ratings

  Returns:
  An integer representing the average user rating of movies of a certain genre
  within a specified source.
  """
  #get ratings list
  movies = get_movies(genre)
  ratings =[]
  for item in movies:
      if item['user_rating']!= None:
        if source in item["source"]:
           ratings.append(item["user_rating"])
      else:
          continue
  return round(statistics.mean(ratings), 2)


#PLOTTING FUNCTIONS
def bar_plot_genre_ratings(genre):
  """
  Generates a bar plot of average rating per genre for the top 5 streaming services.


  Args:
  genre: a string representing the genre we want to analyze

  Returns:
  Nothing, but generates a bar plot
  """
  #data
  height = [get_genre_ratings(genre, "Netflix"),
           get_genre_ratings(genre, "Hulu"),
           get_genre_ratings(genre, "Amazon Prime"),
           get_genre_ratings(genre, "HBO MAX"), 
           get_genre_ratings(genre, "Disney+"), ]
  bars = ["Netflix", "Hulu", "Amazon Prime", "HBO MAX", "Disney+"]
  y_pos = np.arange(len(bars))

  #create bars
  plt.bar(y_pos, height)

  #x axis names
  plt.xticks(y_pos, bars)

  #show plot
  plt.show()

# print(decode_genre("Horror"))
# print(get_genre_ratings("Comedy", "Netflix"))
#print(get_movies("Comedy"))
#merge_files("disneyplustitles.txt", "amazontitles.txt", "netflixtitles.txt", "hbomaxtitles.txt", "hulutitles.txt")