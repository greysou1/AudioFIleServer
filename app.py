# import required packages
from datetime import datetime
from flask import request
from flask.helpers import make_response
import mongo_setup
import flask, json
from flask_cors import CORS, cross_origin
from data.song import song
from data.audiobook import audiobook
from data.podcast import podcast

# initialize our Flask application and the Keras model
app = flask.Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# connect to MongoDB server
mongo_setup.global_init()

@app.route('/create', methods=['POST'])
@cross_origin()
def create():
    '''
    creates a document in the specified audioFileType collection with the given audioFileMetadata
    '''
    # Handling incoming JSON data
    try:
        input = request.get_json()
        audioFileType = input['audioFileType']
        audioFileMetadata = input['audioFileMetadata']
    except:
        return make_response('Bad input. Make sure input is of the type\n\{"audioFileType": "song","audioFileMetadata": \{"ID": 1234, "name": "Circles", "duration": 210\}\} (for song)', 400)

    if audioFileType == 'song':
        # check whether song with specified ID already exists 
        if not song.objects(ID=audioFileMetadata['ID']):
            # create a song object and add metadata to the object
            audiofile = song() 
            audiofile.ID = audioFileMetadata['ID']
            audiofile.name = audioFileMetadata['name']
            audiofile.duration = audioFileMetadata['duration']
            audiofile.save() # insert in the songs collection
        else:
            return make_response(f"Song with ID {audioFileMetadata['ID']} already exists", 400)

        return make_response('Song object successfully created.',200) # Action is successful: 200 OK

    elif audioFileType == 'audiobook':
        # check whether audiobook with specified ID already exists 
        if not audiobook.objects(ID=audioFileMetadata['ID']):
            # create a audiobook object and add metadata to the object
            audiofile = audiobook()
            audiofile.ID = audioFileMetadata['ID']
            audiofile.name = audioFileMetadata['name']
            audiofile.duration = audioFileMetadata['duration']
            audiofile.author = audioFileMetadata['author']
            audiofile.narrator = audioFileMetadata['narrator']
            audiofile.save()# insert in the audiobook collection
        else:
            return make_response(f"Audiobook with ID {audioFileMetadata['ID']} already exists", 400)

        return make_response('Audiobook object successfully created.',200) # Action is successful: 200 OK

    elif audioFileType == 'podcast':
        # check whether podcast with specified ID already exists 
        if not song.objects(ID=audioFileMetadata['ID']):
            # create a podcast object and add metadata to the object
            audiofile = podcast()
            audiofile.ID = audioFileMetadata['ID']
            audiofile.name = audioFileMetadata['name']
            audiofile.duration = audioFileMetadata['duration']
            audiofile.host = audioFileMetadata['host']
            if 'participants' in audioFileMetadata.keys():
                participants = audioFileMetadata['participants']
                if len(participants) < 10:
                    for participant in participants:
                        audiofile.participants.append(participant)
                else:
                    return make_response('Too many participants (more than 10) added.', 400)
            audiofile.save() # insert in the podcast collection
        else:
            return make_response(f"Podcast with ID {audioFileMetadata['ID']} already exists", 400)

        return make_response('Podcast object successfully updated.',200) # Action is successful: 200 OK

    else:
        print("Audio File Type not recognised!")
        return make_response('Audio File Type not recognised!', 400) # The request is invalid: 400 bad request

@app.route('/get/<audioFileType>/<int:audioFileID>', methods=['POST'])
@app.route('/get/<audioFileType>', methods=['POST'])
@cross_origin()
def get(audioFileType, audioFileID = None) -> list:
    '''
    returns a list of dictionaries of all audiofile data of a single collection or of audiofile with specified audioFileID
    '''
    if audioFileType == 'song':
        # query to file the song document with the given audioFileID
        if audioFileID != None:
            query = song.objects().filter(ID=audioFileID)
        else:
            query = song.objects()
        audiofiles = []
        # convert the QuerySet into a readable list of dictionaries 
        for entry in query:
            audiofile = {'ID': entry.ID, 'name': entry.name, 
                    'duration': entry.duration, 'uploaded time': entry.u_time}
            audiofiles.append(audiofile)
        return flask.jsonify(audiofiles), 200 # Action is successful: 200 OK

    elif audioFileType == 'audiobook':
        # query to file the audiobook document with the given audioFileID
        if audioFileID != None:
            query = audiobook.objects().filter(ID=audioFileID)
        else:
            query = audiobook.objects()
        audiofiles = []
        # convert the QuerySet into a readable list of dictionaries
        for entry in query:
            audiofile = {'ID': entry.ID, 'name': entry.name, 
                    'duration': entry.duration, 'uploaded time': entry.u_time,
                    'author': entry.author, 'narrator': entry.narrator}
            audiofiles.append(audiofile)
        return flask.jsonify(audiofiles), 200 # Action is successful: 200 OK

    elif audioFileType == 'podcast':
        # query to file the podcast document with the given audioFileID
        if audioFileID != None:
            query= podcast.objects().filter(ID=audioFileID)
        else:
            query = podcast.objects()
        audiofiles = []
        # convert the QuerySet into a readable list of dictionaries
        for entry in query:
            audiofile = {'ID': entry.ID, 'name': entry.name, 
                    'duration': entry.duration, 'uploaded time': entry.u_time,
                    'host': entry.host, 
                    'participants': [participant for participant in entry.participants]}
            audiofiles.append(audiofile)
        return flask.jsonify(audiofiles), 200 # Action is successful: 200 OK
    else:
        print("Audio File Type not recognised!")
        return make_response('Audio File Type not recognised!', 400) # The request is invalid: 400 bad request

@app.route('/update/<audioFileType>/<int:audioFileID>', methods=['POST'])
@cross_origin()
def update(audioFileType, audioFileID):
    '''
    Updates a document with the specified audioFileType and audioFileID new audioFileMetadata
    '''
    # Handling incoming JSON data
    try:
        audioFileMetadata = request.get_json()
    except:
        return make_response('Bad input. Make sure input is of the type\n\{"ID": 1234, "name": "Despacito", "duration": 210\} (for song)', 400)
    print(audioFileMetadata)
    if audioFileType == 'song':
        song.objects(ID=audioFileID).update(set__ID = audioFileMetadata['ID'], 
                                            set__name = audioFileMetadata['name'],
                                            set__duration = audioFileMetadata['duration'],
                                            set__u_time = datetime.now())
        return make_response('Song object successfully updated.',200) # Action is successful: 200 OK

    elif audioFileType == 'audiobook':
        audiobook.objects(ID=audioFileID).update(set__ID = audioFileMetadata['ID'], 
                                                set__name = audioFileMetadata['name'],
                                                set__duration = audioFileMetadata['duration'],
                                                set__u_time = datetime.now(),
                                                set__author = audioFileMetadata['author'],
                                                set__narrator = audioFileMetadata['narrator'])
        return make_response('Audiobook object successfully updated.',200) # Action is successful: 200 OK

    elif audioFileType == 'podcast':
        podcast.objects(ID=audioFileID).update(set__ID = audioFileMetadata['ID'], 
                                                set__name = audioFileMetadata['name'],
                                                set__duration = audioFileMetadata['duration'],
                                                set__u_time = datetime.now(),
                                                set__host = audioFileMetadata['host'],
                                                set__participants = [participant for participant in audioFileMetadata['participants']])
        return make_response('Podcast object successfully updated.',200) # Action is successful: 200 OK
                                            
    else:
        print("Audio File Type not recognised!")
        return make_response('Audio File Type not recognised!', 400) # The request is invalid: 400 bad request

@app.route('/delete/<audioFileType>/<int:audioFileID>', methods=['POST'])
@cross_origin()
def delete(audioFileType, audioFileID):
    '''
    deletes the document with specified audioFileType and audioFileID
    '''
    if audioFileType == 'song':
        song.objects(ID = audioFileID).delete()
        return make_response('Song object successfully deleted.',200) # Action is successful: 200 OK
    elif audioFileType == 'audiobook':
        audiobook.objects(ID = audioFileID).delete()
        return make_response('Audiobook object successfully deleted.',200) # Action is successful: 200 OK
    elif audioFileType == 'podcast':
        podcast.objects(ID = audioFileID).delete()
        return make_response('Podcast object successfully deleted.',200) # Action is successful: 200 OK
    else:
        print("Audio File Type not recognised!")
        return make_response('Audio File Type not recognised!', 400) # The request is invalid: 400 bad request

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)



# audioFileMetadata1 = {'ID': 1234, 'name': 'Circles', 'duration': 190} # song metadata
# audioFileMetadata2 = {'ID': 1235, 'name': 'Heat wave', 'duration': 250} # song metadata
# audioFileMetadata = {'ID': 1234, 'name': 'New Song', 'duration': 2000, 'host': 'Steve Jobs', 'participants': ['Prudvi', 'Bhanu', 'Sairaj']} # podcast metadata
# audioFileMetadata = {'ID': 1234, 'name': 'New Song', 'duration': 2000, 'author': 'Steve Jobs', 'narrator': 'Tim Cook'} # audiobook metadata

# create('song', audioFileMetadata1)
# create('song', audioFileMetadata2)
# print(get('song'))
# print(get('podcast', 1234))
# update('podcast', 1234, audioFileMetadata)
# delete('song', 1111)