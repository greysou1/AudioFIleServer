from datetime import datetime
import mongoengine

# Creating schema for podcast object
class podcast(mongoengine.Document):
    meta = {
        'db_alias': 'core',
        'collection': 'podcasts'
    }
    ID = mongoengine.IntField(required=True, unique = True)
    name = mongoengine.StringField(required=True, max_length = 100)
    duration = mongoengine.IntField(required=True, min_value=1)
    u_time = mongoengine.DateTimeField(default=datetime.now)
    host = mongoengine.StringField(required=True, max_length = 100)
    participants = mongoengine.ListField(mongoengine.StringField(max_length=100)) #MyListField(mongoengine.StringField(max_length = 100))