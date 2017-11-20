import media
import fresh_tomatoes

avengers = media.Movie("Avengers", "Heroes with superpowers save the world",
                       "https://www.youtube.com/watch?v=udKE1ksKWDE",
                       r"https://orig00.deviantart.net/6be0/f/2011/004/6/f/__the_avengers___poster_2_by_themadbutcher-d36eop9.jpg",  # NOQA
                       "cool")
logan = media.Movie("Logan", "Baby Woulverine saves the day", r"https://www.youtube.com/watch?v=DekuSxJgpbY",  # NOQA
                    r"https://cdn.traileraddict.com/content/20th-century-fox/logan-2017-poster-2.jpg",  # NOQA
                    "freak yeah!")
transformers = media.Movie("Transformers", "Savior turns villain", r"https://www.youtube.com/watch?v=6Vtf0MszgP8",  # NOQA
                           r"https://i0.wp.com/media2.slashfilm.com/slashfilm/wp/wp-content/images/transformers-lastknight-awfulposter-full-700x993.jpg",  # NOQA
                           "supercool")
# Array of the movie objects
movies = [avengers,logan, transformers]
# This function creates the HTML page of movie review website.
fresh_tomatoes.open_movies_page(movies)
