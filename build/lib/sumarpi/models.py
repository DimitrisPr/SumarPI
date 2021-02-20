from gensim.summarization.summarizer import summarize
from tinydb import TinyDB
import json


class Document():
    ''' Class to represent a text/summary object '''

    db = TinyDB('db.json')

    def __init__(self):
        pass

    def generate_summary(self, text):
        self.text = text
        self.summary = summarize(text)

    def save(self):
        ''' Saves current instance to TinyDB
            Returns ID for later retrieval
        '''
        json = {'summary': self.summary}
        self.db.insert(json)
        return self.db.all()[-1].doc_id

    def retrieve_summary(self, id):
        try:
            return self.db.get(doc_id=id)['summary']
        except:
            return None
