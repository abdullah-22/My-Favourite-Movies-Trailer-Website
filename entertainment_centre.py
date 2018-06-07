'''
    This file contains the main function
    that calls another function to make the list of movies from the json file,
    pass this list to fresh_tomatoes file which generated the final webpage
'''

from pathlib import Path
from media import Movie
import fresh_tomatoes


def main():
    # To read movies' data from the json file
    json_path = Path("./movies.json")
    movie_list = Movie.make_movies_list(json_path)

    # To generate the final HTML file and open it in browser
    fresh_tomatoes.create_main_page(movie_list)

main()
