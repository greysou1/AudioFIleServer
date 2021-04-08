# AudioFileServer API

  

API for a simulation of a audio file server that contains audiofiles of types:

### 1. Song
  - ID – (mandatory, integer, unique)
  - Name of the song – (mandatory, string, cannot be larger than 100
  characters)
  - Duration in number of seconds – (mandatory, integer, positive)
  - Uploaded time – (mandatory, Datetime, cannot be in the past)
### 2. Audiobook
  - ID – (mandatory, integer, unique)
  - Title of the audiobook – (mandatory, string, cannot be larger than 100
  characters)
  - Author of the title (mandatory, string, cannot be larger than 100
  characters)
  - Narrator - (mandatory, string, cannot be larger than 100 characters)
  - Duration in number of seconds – (mandatory, integer, positive)
  - Uploaded time – (mandatory, Datetime, cannot be in the past)
### 3. Podcast
  - ID – (mandatory, integer, unique)
  - Name of the podcast – (mandatory, string, cannot be larger than 100
  characters)
  - Duration in number of seconds – (mandatory, integer, positive)
  - Uploaded time – (mandatory, Datetime, cannot be in the past)
  - Host – (mandatory, string, cannot be larger than 100 characters)
  - Participants – (optional, list of strings, each string cannot be larger than
  100 characters, maximum of 10 participants possible)



## Functions
### Create
The request will have the following fields:
  - audioFileType – mandatory, one of the 3 audio types possible
  - audioFileMetadata – mandatory, dictionary, contains the metadata for one
  of the three audio files (song, podcast, audiobook)

POST request at [http://audiofileserver.mooo.com:8000/create](http://audiofileserver.mooo.com:8000/create) along with json data in the format 
`{ "audioFileType": "song", "audioFileMetadata": {"ID": 1234, "name": "Circles", "duration": 210} }`

### Update: 
  - The route be in the following format: “\<audioFileType>/\<audioFileID>”
  - The request body will be the same as the create

POST request at [http://audiofileserver.mooo.com:8000/update](http://audiofileserver.mooo.com:8000/update)/\<audioFileType>/\<int:audioFileID> with json data in format 
`{"ID": 9999, "name": "Despacito", "duration": 210}` 

### Get 
  - The route “\<audioFileType>/\<audioFileID>” will return the specific audio
  file
  - The route “\<audioFileType>” will return all the audio files of that type

POST request at [http://audiofileserver.mooo.com:8000/get](http://audiofileserver.mooo.com:8000/get)/\<audioFileType>/\<int:audioFileID>
or
POST request at [http://audiofileserver.mooo.com:8000/get](http://audiofileserver.mooo.com:8000/get)/\<audioFileType> 
to get all entries

### Delete
  - The route will be in the following format: “\<audioFileType>/\<audioFileID>”

POST request at [http://audiofileserver.mooo.com:8000/delete](http://audiofileserver.mooo.com:8000/delete)/\<audioFileType>/\<int:audioFileID>