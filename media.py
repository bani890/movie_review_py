import webbrowser


class Movie():
    """ A for the movie class"""

    def __init__(self,
                 movie_title,
                 movie_storyline,
                 trailer_url,
                 movie_poster,
                 movie_ratings):
        """ Creates new instances of the classes"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.trailer_youtube_url = trailer_url
        self.poster_image_url = movie_poster
        self.ratings = movie_ratings

    def play_trailer(self):
        """This function plays the trailer from an URL"""
        webbrowser.open(self.url)

    def show_poster(self):
        """This function shows the poster from an URL"""
        webbrowser.open(self.movie_poster)
