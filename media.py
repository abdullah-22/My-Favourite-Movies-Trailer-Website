'''
    This file contains the definition of the "movie" class.
    It will serve as a blueprint for the "movie" type objects.
'''

import json
import webbrowser


class Movie():

    '''
        Attributes:
        -> 'title' (str): for title / name of movie
        -> 'poster_url' (str): for url of poster image of movie
        -> 'trailer_url' (str): for youtube trailer
        -> 'year_of_release' (str): for year of realease of movie
        -> 'director' (str): director name
        -> 'cast' (str): main cast of movie
        -> 'genre' (str): for the genre of movie
        -> 'rating' (str): for movie type rating
        -> 'storyline' (str): for the main theme of story
    '''

    ''' Constructor definition '''
    def __init__(
                 self, title, poster, trailer, year,
                 director, cast, genre, rating, storyline):
            self.title = title
            self.poster_url = poster
            self.trailer_url = trailer
            self.year_of_release = year
            self.director = director
            self.cast = cast
            self.genre = genre
            self.rating = rating
            self.storyline = storyline

    ''' Method to update movie's info by json object values '''
    def update_movie_info(self, movie_info):
        self.title = movie_info['title']
        self.poster_url = movie_info['poster']
        self.trailer_url = movie_info['trailer']
        self.year_of_release = movie_info['year']
        self.director = movie_info['director']
        self.cast = movie_info['cast']
        self.genre = movie_info['genre']
        self.rating = movie_info['rating']
        self.storyline = movie_info['storyline']

    '''
        Method to retrieve movies' information from the json file
        movie-by-key and to return a list of movies.
        The json file is supposed to be created manually
        or as a result of some API response
    '''
    def make_movies_list(file_path):
        movies_list = []

        with open(file_path) as json_file:
            json_data = json.load(json_file)
            for key in json_data:
                value = json_data[key]
                new_movie = Movie(value['title'],
                                  value['poster'],
                                  value['trailer'],
                                  value['year'],
                                  value['director'],
                                  value['cast'],
                                  value['genre'],
                                  value['rating'],
                                  value['storyline'])
                new_movie.update_movie_info(value)
                movies_list.append(new_movie)
        return movies_list

    ''' Method to play the trailer '''
    def play_trailer(self):
        webbrowser.open(self.trailer_url)
