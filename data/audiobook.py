from datetime import datetime
import mongoengine

# Creating schema for audiobook object
class audiobook(mongoengine.Document):
    meta = {
        'db_alias': 'core',
        'collection': 'audiobooks'
    }
    ID = mongoengine.IntField(required=True, unique = True)
    name = mongoengine.StringField(required=True, max_length = 100)
    duration = mongoengine.IntField(required=True, min_value=1)
    u_time = mongoengine.DateTimeField(default=datetime.now)
    author = mongoengine.StringField(required=True, max_length = 100)
    narrator = mongoengine.StringField(required=True, max_length = 100)