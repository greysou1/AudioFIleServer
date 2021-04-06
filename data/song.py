from datetime import datetime
import mongoengine

class song(mongoengine.Document):
    meta = {
        'db_alias': 'core',
        'collection': 'songs'
    }
    ID = mongoengine.IntField(required=True, unique = True)
    name = mongoengine.StringField(required=True)
    duration = mongoengine.IntField(required=True, min_value=1)
    u_time = mongoengine.DateTimeField(default=datetime.now)