from __init__ import db

class Song(db.Model):
    __tablename__ = "Song"
    id = db.Column(db.Integer, primary_key=True)  # Define a primary key column
    character = db.Column(db.String, nullable=False)
    song_name = db.Column(db.String, nullable=False)
    singer = db.Column(db.String, nullable=False)
    era = db.Column(db.String, nullable=False)
    def __init__(self, character, song_name, singer, era):
        self.character = character
        self.song_name = song_name
        self.singer = singer
        self.era = era
    def to_dict(self):
        return {"character": self.character, "song_name": self.song_name, "era": self.era}
def initSongs():
    # You can keep the rest of your code as is
    song1 = Song(character="Walter White", song_name="Changes", singer="David Bowie", era="Innocent"); db.session.add(song1)#replace with real data
    song2 = Song(character="Walter White", song_name="Back in Black", singer="AC/DC", era="Grunge"); db.session.add(song2)
    song3 = Song(character="Walter White", song_name="Baby Blue", singer="Badfinger", era="Prog Rock"); db.session.add(song3)
    db.session.commit()
