import mongo_setup
from data import song, podcast, audiobook

mongo_setup.global_init()

def create(audioFileType, audioFileMetadata):
    if audioFileType == 'song':
        audiofile = song.song()
        audiofile.ID = audioFileMetadata['ID']
        audiofile.name = audioFileMetadata['name']
        audiofile.duration = audioFileMetadata['duration']

        audiofile.save()
        return(audiofile)
        # print(audiofile.get())

audioFileMetadata = {'ID': 1234, 'name': 'Sofia', 'duration': 210}
create('song', audioFileMetadata)
