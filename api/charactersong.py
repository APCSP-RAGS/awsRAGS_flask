from flask import Blueprint, jsonify, request  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random

from model.charactersongs import *

song_api = Blueprint('song_api', __name__, url_prefix='/api/songs')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(song_api)

class songsAPI:
    # not implemented
    class _Create(Resource):
        def post(self, song):
            pass
    # getsongs()
    class _Read(Resource):
        def get(self):
            return jsonify(getSongs())

    # getsong(id)
    class _ReadID(Resource):
        def get(self, id):
            return jsonify(getSong(id))

    # getRandomsong()
    class _ReadRandom(Resource):
        def get(self):
            return jsonify(getRandomSong())
    
    # getRandomsong()
    class _ReadCount(Resource):
        def get(self):
            count = countSongs()
            countMsg = {'count': count}
            return jsonify(countMsg)

    # put method: addsongHaHa
    class _UpdateLike(Resource):
        def put(self, id):
            addSongHaHa(id)
            return jsonify(getSong(id))

    # put method: addsongBooHoo
    class _UpdateJeer(Resource):
        def put(self, id):
            addSongBooHoo(id)
            return jsonify(getSong(id))

    # building RESTapi resources/interfaces, these routes are added to Web Server
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
    api.add_resource(_ReadID, '/<int:id>')
    api.add_resource(_ReadRandom, '/random')
    api.add_resource(_ReadCount, '/count')
    api.add_resource(_UpdateLike, '/like/<int:id>')
    api.add_resource(_UpdateJeer, '/jeer/<int:id>')
    
if __name__ == "__main__": 
    # server = "http://127.0.0.1:5000" # run local
    server = 'https://flask.nighthawkcodingsociety.com' # run from web
    url = server + "/api/songs"
    responses = []  # responses list

    # get count of songs on server
    count_response = requests.get(url+"/count")
    count_json = count_response.json()
    count = count_json['count']

    # update likes/dislikes test sequence
    num = str(random.randint(0, count-1)) # test a random record
    responses.append(
        requests.get(url+"/"+num)  # read song by id
        ) 
    responses.append(
        requests.put(url+"/like/"+num) # add to like count
        ) 
    responses.append(
        requests.put(url+"/jeer/"+num) # add to jeer count
        ) 

    # obtain a random song
    responses.append(
        requests.get(url+"/random")  # read a random song
        ) 

    # cycle through responses
    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")