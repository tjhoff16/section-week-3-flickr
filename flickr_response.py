import json
import unittest
import random


class Photo(object):
    def __init__(self, fdict):
        self.title = fdict['photo']['title']['_content']
        self.artist = fdict['photo']['owner']['username']
        tg = []
        for e in fdict['photo']['tags']['tag']:
            tg.append(e['_content'])
        self.tags = tg
        self.dateuploaded = fdict['photo']['dateuploaded']

    def __str__(self):
        return "{} by {}".format(self.title,self.artist)

    def __repr__(self):
        return

    def __contains__(self):
        return

with open('sample_diction.json', 'r') as f:
    sdict = f.read()
picdict = json.loads(sdict)

pic = Photo(picdict)

print (pic)
