import mongoengine
host = 'mongodb+srv://greysou1:<password>@cluster0.w5sbq.mongodb.net/audio_server?retryWrites=true&w=majority'
def global_init():
    mongoengine.register_connection(alias='core', name='audio_server', host=host)
    