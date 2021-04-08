# Import all required libraries.
import pytest
import requests
from api import decode_source,decode_genre_by_id,fetch_title_data


source_name="Netflix"
id=203
genre_name="Action"
genre_id=1
movie_name="Loyiso Gola: Unlearning"
movie_id=541255

STREAMING_SERVICES=[
("Netflix", 203),
("Hulu",157),
("Amazon Prime",26),
("HBO MAX",387),
("Disney+",372),
("AppleTV+",371),
("BBC iPlayer",409),
("Hayu",392),
("Crave",393),
("IMDB TV",365)
]

MOVIE_GENRES=[
 ("Action", 1),
 ("Action & Adventure",39),
 ("Adventure",2),
 ("Animation",3),
 ("Anime",33),
 ("Comedy",4) ,
 ("Documentary",6),
 ("Biography",31),
 ("Crime",5),
 ("Drama",7)

 
]

MOVIES=[
("Loyiso Gola: Unlearning", 541255),
("RebellComedy: Straight Outta the Zoo",541215),
("Murder Among the Mormons",541153),
("Nate Bargatze: The Greatest Average American",541124),
("Fate: The Winx Saga - The Afterparty",541123),
("Making the Witcher",541085),
("North Korea: Inside The Mind of a Dictator",541110),
("Dr. Seuss' The Grinch Musical",540894),
("Black Narcissus",540790),
("Little Fires Everywhere",538254),


]

@pytest.mark.parametrize("source_name,id", STREAMING_SERVICES)
def test_source_ids(source_name, id):
    """
    Check that the source name given yields the source id given as a parameter

    Args:
        source_name: A string representing the name of a streaming service.
        id: the id representing the id of a streaming service.
    """
    assert decode_source(source_name) == id

@pytest.mark.parametrize("genre_name,genre_id", MOVIE_GENRES)
def test_genre(genre_name, genre_id):
    """
    Check that the genre name given yields the  genre_id given as a parameter

    Args:
        genre_name: A string representing the name of a genre.
        genre_id: the genre_id.
    """
    assert decode_genre_by_id(genre_name) == genre_id


@pytest.mark.parametrize("movie_name,movie_id", MOVIES)
def test_movie_title(movie_name, movie_id):
    """
    Check that the id provided returns a certain movie title

    Args:
        genre_name: A string representing the name of a movie.
        movie_id: A string representing the id of a movie.
    """
    movie=fetch_title_data(movie_id,3) 
    assert movie['title'] == movie_name