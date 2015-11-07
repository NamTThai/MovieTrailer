import urllib2
import json


class Movie():
    """This class holds all the information about movie"""
    def __init__(self, title, poster_image_url, trailer_youtube_url, imdb_id):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.imdb_id = imdb_id
        self.__getImdbData(self.imdb_id)

    def __getImdbData(self, imdb_id):
        """
        Launch HTTP GET request to retrieve IMDB data using IMDB ID and OMDB
        API. This method can be improved by launching asynchronous request.
        However it is unnecessary since each request takes minimum time.
        """
        url = "http://www.omdbapi.com/?plot=short&r=json&i=" + imdb_id
        try:
            imdb_data = json.load(urllib2.urlopen(url))
            self.imdb_rating = imdb_data["imdbRating"]
            self.imdb_votes = imdb_data["imdbVotes"]
        except urllib2.URLError:
            self.imdb_rating = "0.0"
            self.imdb_votes = "0"
