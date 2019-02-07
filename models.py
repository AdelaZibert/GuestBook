from google.appengine.ext import ndb

class Message(ndb.Model):
    text = ndb.StringProperty()
    rating = ndb.IntegerProperty()
    name = ndb.StringProperty()
    rating_color = ndb.StringProperty()
