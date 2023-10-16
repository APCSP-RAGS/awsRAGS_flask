from __init__ import db

class Song(db.Model):
    __tablename__ = "Song"
    id = db.Column(db.Integer, primary_key=True)  # Define a primary key column
    character = db.Column(db.Stri+ng, nullable=False)
    song_name = db.Column(db.String, nullable=False)
    era = db.Column(db.String, nullable=False)
    def __init__(self, character, song_name, era):
        self.character = character
        self.song_name = song_name
        self.era = era
    def to_dict(self):
        return {"character": self.character, "song_name": self.song_name, "era": self.era}
def init_Songs():
    # You can keep the rest of your code as is
    song1 = Song(character="Walter White", song_name="Song 1", era="Innocent"); db.session.add(song1)#replace with real data
    song2 = Song(character="Walter White", song_name="Song 2", era="Grunge"); db.session.add(song2)
    song3 = Song(character="Walter White", song_name="Song 3", era="Prog Rock"); db.session.add(song3)
    db.session.commit()
