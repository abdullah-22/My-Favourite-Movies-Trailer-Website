'''
    Contains the script to generate the main HTML page,
'''

import webbrowser
import os
import re

# Get the HTML contents templates

# HTML header template
with open('templates/header.html', 'r') as header:
    main_page_head = header.read()


# HTML body template
with open('templates/body.html', 'r') as body:
    main_page_content = body.read()


# HTML movie tile template for single item
with open('templates/movie_tile.html', 'r') as tile:
    movie_tile_content = tile.read()


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_url)  # NOQA

        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None  # NOQA

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_poster=movie.poster_url,
            movie_trailer=trailer_youtube_id,
            movie_year=movie.year_of_release,
            movie_director=movie.director,
            movie_cast=movie.cast,
            movie_genre=movie.genre,
            movie_rating=movie.rating,
            movie_storyline=movie.storyline,
        )
    return content


def create_main_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the placeholder for the movie tiles
    # with the actual dynamically generated content
    rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))  # NOQA

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)  # open in a new tab, if possible
