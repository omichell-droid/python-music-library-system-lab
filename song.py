class Song:
    """A song in the music library that also tracks stats about all songs."""

    # Class attributes: shared by every Song
    count = 0          # total number of songs created
    genres = []        # unique genres
    artists = []       # unique artists
    genre_count = {}   # e.g. {"Rap": 5, "Rock": 1}
    artist_count = {}  # e.g. {"Beyonce": 17, "Jay-Z": 40}
    artists_count = artist_count  # same dict, under the name used in the instructions

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update the class-wide stats every time a song is created
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artist_count(cls, artist):
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1
        cls.artists_count = cls.artist_count  # keep both names pointing at the same dict

    # Alias so the method also works under the name used in the instructions
    @classmethod
    def add_to_artists_count(cls, artist):
        cls.add_to_artist_count(artist)