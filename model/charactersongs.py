from __init__ import db

class Song(db.Model):
    __tablename__ = "Song"
    id = db.Column(db.Integer, primary_key=True)  # Define a primary key column
    character = db.Column(db.String, nullable=False)
    song_name = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    def __init__(self, character, song_name, artist, genre):
        self.character = character
        self.song_name = song_name
        self.artist = artist
        self.genre = genre
    def to_dict(self):
        return {"character": self.character, "song_name": self.song_name, "artist": self.artist, "genre": self.genre}
def initSongs():
    # You can keep the rest of your code as is
    song1 = Song(character="Walter White", song_name="Changes", artist="David Bowie", genre="Art Pop"); db.session.add(song1)#replace with real data
    song2 = Song(character="Walter White", song_name="Back in Black", artist="AC/DC", genre="Hard Rock"); db.session.add(song2)
    song3 = Song(character="Walter White", song_name="Baby Blue", artist="Badfinger", genre="Rock"); db.session.add(song3)
    song4 = Song(character="Walter White", song_name="A Horse with No Name", artist="America", genre="Soft Rock"); db.session.add(song4)
    db.session.commit()
