import urllib.request
import json
import statistics
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
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


def decode_source(source):
  """
  Gives the source id for a streaming service of a certain name. This helps
  with API calls as the source id is needed to fetch data straight from the API

  Args:
  source: a string representing the name of the streaming service (i.e.
  Netflix, HBO MAX)

  Returns:
  An integer representing the id of the source in the API.
  """

  with open("sources.txt") as json_file:
    source_data = json.load(json_file)
    specific_source = [item for item in source_data if item["name"] == source]
    source_id = specific_source[0]["id"]
  return source_id




def fetch_title_data(id,count):
    """
    This function takes in an id of a movie and sends a request to the
    watchmode api to get the details of the movie. The API response is a
    dictionary with all the details of said movie.

    Args:
    id: a string representing the id of the movie

    Returns:
    The function returns a dictionary with all the relevant details of a movie
    
    """
    current_api_key=testApi6
    if count % 2 ==0:
       current_api_key=testApi6
    else:
       current_api_key=testApi7

    with urllib.request.urlopen(f"https://api.watchmode.com/v1/title/{id}/details/?apiKey={current_api_key}") as url:
        data = json.loads(url.read().decode())
        #print(data)
        if data:
          return data
        return

def fetch_list_title_data(source_id):
    """
    
    This function takes in a source id as a parameter and  sends a request to
    the watchmode api to get a list of all the movies from a certain source
    (Netflix,HBO MAX). Since the watchmode API returns data in pages, the
    function iterates through all the pages untill it has gotten all the data
    from that particular source.

    Args:
    source_id: an integer representing the id of the streaming service

    Returns:
    The function returns a list of all the movies that exist in that particular source

    """
    movies_array=[]
    total_pages=34
    page=1
    while page<=total_pages:
        with urllib.request.urlopen(f"https://api.watchmode.com/v1/list-titles/?apiKey={apiKey3}&source_ids={source_id}&page={page}") as url:
          data = json.loads(url.read().decode())
          #print(page)
          movies_array+=data["titles"]
          page+=1
    return movies_array


def fetch_and_write_title_ids_to_file(source, filename):
  """

  This function writes all the movies from a specific source into one file.
  Once the `fetch_list_title_data` gets information from the watchmode API,
  this function then writes that data into a file.

  Args:
  source: a string representing the name of the source.
  filename: a string representing the file into which the data will be written

  Returns:
  Nothing, but writes the API data into the file.
  """

  source_id = decode_source(source)
  data=fetch_list_title_data(source_id) #decode id
  with open(filename, 'w') as outfile:
    json.dump(data, outfile)

def fetch_title_details(srcfile,source):
    """

    This function utilises `fetch_title_data` to fetch data from the watchmode
    api, it then iterates through the list of dictionaries and appends the
    source attribute to each dictionary.

    Args:
      srcfile:  This is the source file to get data on all the movie titles
      source: This is the name of the streaming service i.e Netflix

    Returns:
    The function returns a list of all of the movies with the service appended.

    """ 
    with open(srcfile) as json_file:
     data = json.load(json_file)
     titles=[]
     count=0
     for i in data:
       if count <=200:
        #print(count) 
        title= fetch_title_data(i['id'],count)
        title['source']= source
        titles.append(title)
        count+=1
       else:
         break 
     return titles

def save_title_details_data(source_file, service, new_file):
    """

    This function writes all the movies titles from a specific source into one
    file. Once the `fetch_title_details` gets information from the watchmode
    API, this function then writes that data into a file.

    Args:
      source_file: a string with the file name, including the extension
      (i.e. "netflix.txt")
      service: a string representing the name of the streaming service
      (i.e. "Netflix")
      new_file: a string representing the name of the new file in which the
      API data will be locally stored.
    
    """
    data=fetch_title_details(source_file, service)
    with open(new_file, 'w') as outfile:
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
  if len(movies) == 0:
    # print(f"There are no {genre} movies or shows across all 5 services")
    return 0
  else:
    for item in movies:
        if item['user_rating']!= None:
          if source in item["source"]:
            ratings.append(item["user_rating"])
        else:
            continue
    #edge case, there are no movies of that genre
    if len(ratings) == 0:
      print(f"No {genre} movies found in {source}")
      average_rating = 0
    else:
      average_rating = statistics.mean(ratings)
    return round(average_rating, 2)
    


def genres_list():
  """
  Shows a list of genres so that users can experiment with genre-based functions

  Args:
  none

  Returns:
  none but prints a list of the valid genres that can be inputted into the
  functions of this project.
  """
  genre_list = []
  with open("genre.txt") as json_file:
    genre_data = json.load(json_file)

    for item in genre_data:
        genre_list.append(item["name"])
        genre_list_easy_read = '\n'.join(genre_list)
    print(genre_list_easy_read)


def number_of_movies(genre, source):
  """
  Counts the number of movies in a specific genre within a single source.

  Args:
  genre: a string representning the genre which we want to explore
  source: a string representing the streaming service within which we are
  counting the movies/shows.

  Returns:
  An integer representing how many movies of a certain genre the inputted
  source carries.
  """
  #movies of a genre
  movies = get_movies(genre)
  count = 0
  
  #iterate through movies
  for item in movies:
    #iterate through only one source
    if source in item["source"]:
      count += 1
    else:
      continue
  return count



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
  #check that there are movies
  movies = get_movies(genre)
  if len(movies) == 0:
    print(f"There are no {genre} movies or shows across all 5 services")
  
  height = [get_genre_ratings(genre, "Netflix"),
           get_genre_ratings(genre, "Hulu"),
           get_genre_ratings(genre, "Amazon Prime"),
           get_genre_ratings(genre, "HBO MAX"), 
           get_genre_ratings(genre, "Disney Plus"), ]
  bars = ["Netflix", "Hulu", "Amazon Prime", "HBO MAX", "Disney+"]
  y_pos = np.arange(len(bars))

  #create bars
  plt.bar(y_pos, height)

  #x axis names
  plt.xticks(y_pos, bars)

  #titles
  plt.title(f"Average Media Rating for {genre}")
  plt.xlabel("Streaming Service")
  plt.ylabel("Average User Rating (out of 10)")

  #show plot
  plt.show()

def scatter_plot_genre(genre):
  """
  Displays a scatter plot of the media across the top 5 streaming services for
  a specific genre.

  Args:
  genre: a string representing the genre we want to explore

  Returns:
  Nothing, but displays a scatter plot of the services vs genres, 
  """
  #data
  quantities = [number_of_movies(genre, "Netflix"),
           number_of_movies(genre, "Hulu"),
           number_of_movies(genre, "Amazon Prime"),
           number_of_movies(genre, "HBO MAX"), 
           number_of_movies(genre, "Disney Plus"), ]

  ratings = [get_genre_ratings(genre, "Netflix"),
           get_genre_ratings(genre, "Hulu"),
           get_genre_ratings(genre, "Amazon Prime"),
           get_genre_ratings(genre, "HBO MAX"), 
           get_genre_ratings(genre, "Disney Plus"), ]

  labels = ["Netflix", "Hulu", "Amazon Prime", "HBO MAX", "Disney Plus"]

  #plot
  plt.scatter(quantities, ratings)

  #label points
  for i, txt in enumerate(labels):
    plt.annotate(txt, (quantities[i], ratings[i]))
  
  #titles
  plt.xlabel("Number of Movies/Shows in Genre")
  plt.ylabel("Average Rating of Movies in Genre")
  plt.title("Average Rating of Movies vs. Amount of Movies in Genre")

def bubble_plot_genre(genre, student=False):
  """
  Displays a bubble plot of the media across the top 5 streaming services for
  a specific genre. The size of the bubbles is determined by how many movies
  of that genre the service carries. Note that these are the prices for the
  "basic" plans. More expensive options are available, but the number of movies
  stays the same.

  Args:
  genre: a string representing the genre we want to explore
  student: a boolean which allows the user to choose whether they want to see
  the prices for students or non-students. This option is due to the fact that
  students often get discounts on streaming services, so the price is not the
  same for them.

  Returns:
  Nothing, but displays a bubble plot of the services vs genres, with bubble
  size determined by the quantity of movies/shows the service has.
  """

  #data
  quantities = [number_of_movies(genre, "Netflix"),
          number_of_movies(genre, "Hulu"),
          number_of_movies(genre, "Amazon Prime"),
          number_of_movies(genre, "HBO MAX"),
          number_of_movies(genre, "Disney Plus"), ]

  ratings = [get_genre_ratings(genre, "Netflix"),
          get_genre_ratings(genre, "Hulu"),
          get_genre_ratings(genre, "Amazon Prime"),
          get_genre_ratings(genre, "HBO MAX"), 
          get_genre_ratings(genre, "Disney Plus"), ]
  labels = ["Netflix", "Hulu", "Amazon Prime", "HBO MAX", "Disney Plus"]

  if student == True:
    prices = [8.99, 2, 8.99, 14.99, 7.99]
  else:
    prices = [8.99, 6, 6.49, 14.99, 7.99]
  


  #plot
  plt.scatter(quantities, ratings, c=sorted(prices), alpha=0.5,
              s = [price*100 for price in prices])

  #label points
  for i, txt in enumerate(labels):
    plt.annotate(txt, (quantities[i], ratings[i]))
  
  #titles
  plt.xlabel("Number of Movies/Shows in Genre")
  plt.ylabel(f"Average Rating of Movies in {genre} Genre")
  plt.title(f"Average Rating of Movies vs. Amount of Movies in {genre} Genre")

  #bubble plot is just scatter with variable bubble sizes

# def circular_barplot_prices(student=False):
#   """
#   Plots a circular barplot to show the prices of the streaming services.

#   Args:
#   No required arguments
#   student: a boolean value for whether you want to see the regular prices or
#   the special student prices. These prices are the cost per month.

#   Returns:
#   Nothing, but generates a circular barplot.
#   """
#   if student == True:
#     prices = [8.99, 2, 8.99, 14.99, 7.99]
#   else:
#     prices = [8.99, 6, 6.49, 14.99, 7.99]

#   labels = ["Netflix", "Hulu", "Amazon Prime", "HBO MAX", "Disney Plus"]
#   max_price = max(prices)
#   print(max_price)

#   #plotting time
#   ax = plt.subplot(111, polar=True)
#   plt.axis("off")

#   width = 2*np.pi / len(prices)
#   indexes=list(range(1, len(prices)+1))
#   angles = [element * width for element in indexes]

#   #coordinate limits?
#   #draw bars
#   bars = ax.bars(
#     x=angles,
#     height=labels,
#     width=width,
#     bottom=0,
#     linewidth=2,
#     edgecolor="white")


# save_title_details_data()

#STATEMENTS FOR FUNCTION TESTING
#print(decode_source("Hulu"))
# merge_files('amazontitles1.txt','disneyplustitles1.txt','hbomaxtitles1.txt','hulutitles1.txt','netflixtitles1.txt','movie_details_list1.txt')
#print(number_of_movies("Horror", "Disney Plus"))
# print(decode_genre("Horror"))
# print(get_genre_ratings("Comedy", "Disney +"))
#genres_list()
# print(get_movies("Comedy"))
