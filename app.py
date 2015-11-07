from movie import Movie
import fresh_tomatoes
import json

# Load a json file containing movie information
with open('data/movies.json') as data_file:
    data = json.load(data_file)

# Initialize movie instances and store them in movies list
movies = []
for movie_id in data:
    movie_data = data[movie_id]
    movie = Movie(movie_data["title"], movie_data["posterImageUrl"], movie_data["trailerYoutubeUrl"], movie_data["imdbId"])
    movies.append(movie)

# Open static HTML web page with all movie instances
fresh_tomatoes.open_movies_page(movies)
