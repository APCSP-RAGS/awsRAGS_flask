from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource, reqparse
from __init__ import db
from model.charactersongs import Song  # Import the song model
import requests

# Create a Blueprint for the song API
song_api = Blueprint('song_api', __name__, url_prefix='/api/song')

# Create the API instance
api = Api(song_api)

class SongAPI:
    class _Create(Resource):
        def post(self):
            # get request body
            body = request.get_json()
            # get variables
            character = body.get('character')
            song_name = body.get('song_name')
            artist = body.get('artist')
            genre = body.get('genre')
            lyrics = body.get('lyrics')
            # Set up Song class object
            song_obj = Song(character=character, song_name=song_name, artist=artist, genre=genre, lyrics=lyrics)
            
            ''' #2: Key Code block to add song to database '''
            # create song in database
            song = song_obj.create()
            # success returns json of song
            if song:
                return jsonify(song.read())
            # failure returns error
            return {'message': f'Invalid input, correct fields should be character, song_name, artist, and genre'}, 400

            
    class _Read(Resource):
        def get(self):
        # Retrieve all songs from the database
            songs = Song.query.all()
            json_ready = [song.to_dict() for song in songs]
        # Return the JSON response
            return jsonify(json_ready)

    # building RESTapi resources/interfaces, these routes are added to Web Server
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
