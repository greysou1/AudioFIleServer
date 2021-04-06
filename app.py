# import required packages
from datetime import datetime
import mongo_setup
from data.song import song
from data.audiobook import audiobook
from data.podcast import podcast

# connect to MongoDB server
mongo_setup.global_init()

def create(audioFileType, audioFileMetadata):
    '''
    creates a document in the specified audioFileType collection with the given audioFileMetadata
    '''
    if audioFileType == 'song':
        # create a song object and add metadata to the object
        audiofile = song() 
        audiofile.ID = audioFileMetadata['ID']
        audiofile.name = audioFileMetadata['name']
        audiofile.duration = audioFileMetadata['duration']
        audiofile.save() # insert in the songs collection

    elif audioFileType == 'audiobook':
        # create a audiobook object and add metadata to the object
        audiofile = audiobook()
        audiofile.ID = audioFileMetadata['ID']
        audiofile.name = audioFileMetadata['name']
        audiofile.duration = audioFileMetadata['duration']
        audiofile.author = audioFileMetadata['author']
        audiofile.narrator = audioFileMetadata['narrator']
        audiofile.save()# insert in the audiobook collection

    elif audioFileType == 'podcast':
        # create a podcast object and add metadata to the object
        audiofile = podcast()
        audiofile.ID = audioFileMetadata['ID']
        audiofile.name = audioFileMetadata['name']
        audiofile.duration = audioFileMetadata['duration']
        audiofile.host = audioFileMetadata['host']
        participants = audioFileMetadata['participants']
        ### fix to accept only 10 participants in list
        for participant in participants:
            audiofile.participants.append(participant)
        audiofile.save() # insert in the podcast collection
    
    else:
        print("Audio File Type not recognised!")
        return

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
        return audiofiles

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
        return audiofiles

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
        return audiofiles
    else:
        print("Audio File Type not recognised!")
        return

def update(audioFileType, audioFileID, audioFileMetadata):
    '''
    Updates a document with the specified audioFileType and audioFileID new audioFileMetadata
    '''
    if audioFileType == 'song':
        song.objects(ID=audioFileID).update(set__ID = audioFileMetadata['ID'], 
                                            set__name = audioFileMetadata['name'],
                                            set__duration = audioFileMetadata['duration'],
                                            set__u_time = datetime.now())
        print('Song object updated.')

    elif audioFileType == 'audiobook':
        audiobook.objects(ID=audioFileID).update(set__ID = audioFileMetadata['ID'], 
                                                set__name = audioFileMetadata['name'],
                                                set__duration = audioFileMetadata['duration'],
                                                set__u_time = datetime.now(),
                                                set__author = audioFileMetadata['author'],
                                                set__narrator = audioFileMetadata['narrator'])
        print('Audiobook object updated.')

    elif audioFileType == 'podcast':
        podcast.objects(ID=audioFileID).update(set__ID = audioFileMetadata['ID'], 
                                                set__name = audioFileMetadata['name'],
                                                set__duration = audioFileMetadata['duration'],
                                                set__u_time = datetime.now(),
                                                set__host = audioFileMetadata['host'],
                                                set__participants = [participant for participant in audioFileMetadata['participants']])
        print('Podcast object updated.')
                                            
    else:
        print("Audio File Type not recognised!")
        return

def delete(audioFileType, audioFileID):
    '''
    deletes the document with specified audioFileType and audioFileID
    '''
    if audioFileType == 'song':
        song.objects(ID = audioFileID).delete()
    elif audioFileType == 'audiobook':
        audiobook.objects(ID = audioFileID).delete()
    elif audioFileType == 'podcast':
        podcast.objects(ID = audioFileID).delete()
    else:
        print("Audio File Type not recognised!")
        return

audioFileMetadata1 = {'ID': 1234, 'name': 'Circles', 'duration': 190} # song metadata
audioFileMetadata2 = {'ID': 1235, 'name': 'Heat wave', 'duration': 250} # song metadata
# audioFileMetadata = {'ID': 1234, 'name': 'New Song', 'duration': 2000, 'host': 'Steve Jobs', 'participants': ['Prudvi', 'Bhanu', 'Sairaj']} # podcast metadata
# audioFileMetadata = {'ID': 1234, 'name': 'New Song', 'duration': 2000, 'author': 'Steve Jobs', 'narrator': 'Tim Cook'} # audiobook metadata

# create('song', audioFileMetadata1)
# create('song', audioFileMetadata2)
print(get('song'))
# print(get('podcast', 1234))
# update('podcast', 1234, audioFileMetadata)
# delete('song', 1111)