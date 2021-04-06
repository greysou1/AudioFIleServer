# AudioFileServer

  

Simulation of a audio file server contains audiofiles of types

1. Song
2. Audiobook
3. Podcast


## Functions
### Create
POST request at [192.46.210.223/create](http://audiofileserver.mooo.com:8000/create) along with json data in the format 
`{ "audioFileType": "song", "audioFileMetadata": {"ID": 1234, "name": "Circles", "duration": 210} }`
### Update: 
POST request at [192.46.210.223/update](http://audiofileserver.mooo.com:8000/update)/\<audioFileType>/\<int:audioFileID> with json data in format 
`{"ID": 9999, "name": "Despacito", "duration": 210}` 
### Get 
POST request at [192.46.210.223/get](http://audiofileserver.mooo.com:8000/get)/\<audioFileType>/\<int:audioFileID>
or
POST request at [192.46.210.223/get](http://audiofileserver.mooo.com:8000/get)/\<audioFileType> 
to get all entries
### Delete
POST request at [192.46.210.223/delete](http://audiofileserver.mooo.com:8000/delete)/\<audioFileType>/\<int:audioFileID>