class Song:
    """ Class to represent a song

    Attributes:
        title (str): The title of the song
        artist (Artist): An artist object representing the song's creator.
        duration (int): The duration of the song in seconds. May be zero.
    """

    def __init__(self, title, artist, duration=0):
        """Song init method

        Args:
            title (str): Initalise the 'title' attribute
            artist (Artist): An Artist object representing the song's creator.
            duration (Optional[int]: Initial value for the 'duration' attribute.
                Will default to zero is not specified.
        """
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """Class to represent an Album, using it's track list

    Attributes:
        album_name (str) : The name of the album.
        year (int): The year the album was released.
        artist: (Artist): The artist respinsible for the album.
            If not specified, the artist will default to an artist with the name
            "Various Artists".
        tracks (List[Song]): A list of the songs on the album.

    Methods:
        addSong: Used to add a new song to the album's track list.
    """
