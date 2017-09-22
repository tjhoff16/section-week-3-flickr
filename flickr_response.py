import json
import unittest
import random


class Photo(object):
    def __init__(self, fdict):
        self.title = fdict['photo']['title']['_content']
        self.artist = fdict['photo']['owner']['username']
        self.tags = []
        for e in fdict['photo']['tags']['tag']:
            self.tags.append(e['_content'])
        self.dateuploaded = fdict['photo']['dateuploaded']
        self.ID = fdict['photo']['id']
    def __str__(self):
        return "{0} by {1}".format(self.title,self.artist)

    def __repr__(self):
        return "Photo(title={0}, artist={1}, tags={2}, date={3}, ID={4})".format(self.title,self.artist,self.tags,self.dateuploaded,self.ID)

    def __contains__(self):
        return

with open('sample_diction.json', 'r') as f:
    sdict = f.read()
picdict = json.loads(sdict)

pic = Photo(picdict)

print (repr(pic))
