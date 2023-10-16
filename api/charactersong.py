from flask import Blueprint, jsonify
from flask_restful import Api, Resource, reqparse
from __init__ import db
from model.charactersongs import Song  # Import the song model

# Create a Blueprint for the song API
song_api = Blueprint('song_api', __name__, url_prefix='/api/song')

# Create the API instance
api = Api(song_api)

class songAPI(Resource):
    def get(self, id):
        # Retrieve a single song by its ID from the database
        song = Song.query.get(id)

        if song:
            return song.to_dict(), 200
        else:
            return {"message": "song not found"}, 404

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("character", type=str)
        parser.add_argument("song_name", type=str)
        parser.add_argument("era", type=str)
        args = parser.parse_args()

        try:
            song = db.session.query(song).get(id)
            if song:
                if args["song_name"] is not None:
                    song.song_name = args["song_name"]
                if args["character"] is not None:
                    song.character = args["character"]
                if args["era"] is not None:
                    song.era = args["era"]
                db.session.commit()
                return song.to_dict(), 200
            else:
                return {"message": "song not found"}, 404
        except Exception as exception:
            db.session.rollback()
            return {"message": f"Error: {exception}"}, 500

    def delete(self, id):
        try:
            song = db.session.query(song).get(id)
            if song:
                db.session.delete(song)
                db.session.commit()
                return song.to_dict()
            else:
                return {"message": "song not found"}, 404
        except Exception as exception:
            db.session.rollback()
            return {"message": f"Error: {exception}"}, 500

# Add the songAPI resource to the /api/song/<int:id> endpoint
api.add_resource(songAPI, "/<int:id>")

class songListAPI(Resource):
    def get(self):
        # Retrieve all songs from the database
        songs = Song.query.all()

        # Prepare the data in JSON format
        json_ready = [song.to_dict() for song in songs]

        # Return the JSON response
        return jsonify(json_ready)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("song_name", required=True, type=str)
        parser.add_argument("character", required=True, type=str)
        parser.add_argument("era", required=True, type=str) 
        args = parser.parse_args()
        song = song(args["song_name"], args["character"], args["era"], args["price"])

        try:
            db.session.add(song)
            db.session.commit()
            return song.to_dict(), 201
        except Exception as exception:
            db.session.rollback()
            return {"message": f"Error: {exception}"}, 500

# Add the songListAPI resource to the /api/song endpoint
api.add_resource(songListAPI, "/")