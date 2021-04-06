from datetime import datetime
import mongoengine

class audiobook(mongoengine.Document):
    meta = {
        'db_alias': 'core',
        'collection': 'audiobooks'
    }
    def __init__(self, metadata):
        self.ID = mongoengine.IntField(required=True, unique = True)
        self.name = mongoengine.StringField(required=True, max_length = 100)
        self.duration = mongoengine.IntField(required=True, min_value=1)
        self.u_time = mongoengine.DateTimeField(default=datetime.now)
        self.author = mongoengine.StringField(required=True, max_length = 100)
        self.narrator = mongoengine.StringField(required=True, max_length = 100)

    def get(self):
        return({'ID': self.ID, 'Name': self.name, 
                'Duration in seconds': self.duration, 
                'Uploaded time': self.u_time.strftime('%Y-%m-%d %H:%M:%S'),
                'Author of the title': self.author,
                'Narrator': self.narrator})