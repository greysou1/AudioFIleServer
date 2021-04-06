from datetime import datetime
import mongoengine

class MyListField(mongoengine.ListField):
    def __init__(self, max_length=None,  **kwargs):
        self.max_length = max_length
        super(MyListField, self).__init__(**kwargs)

    def validate(self, value):
        super(MyListField, self).validate(value)

        if self.max_length is not None and len(value) > self.max_length:
            self.error('Too many items in the list')

class podcast(mongoengine.Document):
    meta = {
        'db_alias': 'core',
        'collection': 'podcasts'
    }
    def __init__(self, metadata):
        self.ID = mongoengine.IntField(required=True, unique = True)
        self.name = mongoengine.StringField(required=True, max_length = 100)
        self.duration = mongoengine.IntField(required=True, min_value=1)
        self.u_time = mongoengine.DateTimeField(default=datetime.now)
        self.host = mongoengine.StringField(required=True, max_length = 100)
        self.participants = MyListField(mongoengine.StringField(max_length = 100), max_length=10)

    def get(self):
        return({'ID': self.ID, 'Name': self.name, 
                'Duration': self.duration, 
                'Uploaded time': self.u_time.strftime('%Y-%m-%d %H:%M:%S'),
                'Host': self.host,
                'Participants': self.participants})