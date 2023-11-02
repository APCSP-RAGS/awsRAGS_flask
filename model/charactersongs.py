from __init__ import db
from lyricsgenius import Genius

token = "LicaWYTkX6bWFSV8c1QlTl7O9gLPZh7TvO3ZpR9OOwYe_GajHsIEebEvppPhY9V7"

genius = Genius(token)

genius.excluded_terms = ["Contributors", "Lyrics"]

class Song(db.Model):
    __tablename__ = "Song"
    id = db.Column(db.Integer, primary_key=True)  # Define a primary key column
    character = db.Column(db.String, nullable=False) # Breaking bad character
    song_name = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    lyrics = db.Column(db.String, nullable=False)
    def __init__(self, character, song_name, artist, genre, lyrics): # Constructer 
        self.character = character
        self.song_name = song_name
        self.artist = artist
        self.genre = genre
        self.lyrics = lyrics
    # Convert db data to a dictionary in order to return easily using JSON
    def to_dict(self):
        return {"character": self.character, "song_name": self.song_name, "artist": self.artist, "genre": self.genre, "lyrics": self.lyrics}
    # Create method to let users add a song to the DB
    def create(self):
        try:
            try:
                self.lyrics = genius.search_song(self.song_name, self.artist).lyrics.split("Lyrics")[1]
            except:
                self.lyrics = "Check that the artist name and song anme are spelled correctly"
            db.session.add(self)  # add prepares to persist object to table
            db.session.commit()  # SQLAlchemy requires a manual commit
            return self
        except: 
            db.session.remove() # remove object from table if invalid
            return None
    # Read method to return every part of the table
    def read(self):
        return {
            "id": self.id,
            "character": self.character,
            "song_name": self.song_name,
            "artist": self.artist,
            "genre": self.genre,
            "lyrics": self.lyrics
        }


# Initialize songs

def initSongs():
    # Adds each song + its metadata to the db
    song1 = Song(character="Walter White", song_name="Changes", artist="David Bowie", genre="Art Pop", lyrics=genius.search_song("Changes", "David Bowie").lyrics.split("Lyrics")[1]); db.session.add(song1)#replace with real data
    song2 = Song(character="Walter White", song_name="Back in Black", artist="AC/DC", genre="Hard Rock", lyrics=genius.search_song("Back in Black", "AC/DC").lyrics.split("Lyrics")[1]); db.session.add(song2)
    song3 = Song(character="Walter White", song_name="Baby Blue", artist="Badfinger", genre="Rock", lyrics=genius.search_song("Baby Blue", "Badfinger").lyrics.split("Lyrics")[1]); db.session.add(song3)
    # song4 = Song(character="Walter White", song_name="A Horse with No Name", artist="America", genre="Soft Rock"); db.session.add(song4)
    # song5 = Song(character="Walter White", song_name="Crystal Blue Persuasion", artist="Tommy James and the Shondells", genre="Rock"); db.session.add(song5)
    # song6 = Song(character="Walter White", song_name="Sweet Home Alabama", artist="Lynyrd Skynyrd", genre="Southern Rock"); db.session.add(song6)
    # song7 = Song(character="Walter White", song_name="God's Gonna Cut You Down", artist="Johnny Cash", genre="Country"); db.session.add(song7)
    # song8 = Song(character="Walter White", song_name="Break on Through (To the Other Side)", artist="The Doors", genre="Rock"); db.session.add(song8)
    # song9 = Song(character="Walter White", song_name="Hurt", artist="Nine Inch Nails", genre="Industrial Rock"); db.session.add(song9)
    # song10 = Song(character="Walter White", song_name="Street Spirit (Fade Out)", artist="Radiohead", genre="Alternative Rock"); db.session.add(song10)
    # song11 = Song(character="Walter White", song_name="Comfortably Numb", artist="Pink Floyd", genre="Progressive Rock"); db.session.add(song11)
    # song12 = Song(character="Walter White", song_name="Baby, I'm Howlin' for You", artist="The Black Keys", genre="Blues Rock"); db.session.add(song12)
    # song13 = Song(character="Walter White", song_name="Blue Moon", artist="Beck", genre="Alternative"); db.session.add(song13)
    db.session.commit()
