#!/usr/bin/env python
#-*- coding: utf-8 -*-

import urllib2
import urllib
import pprint
import simplejson as json
import re
from properties.properties import *

class Translator:
    def __init__(self, word):
        self.englishMeanings = []
        self.turkishMeanings = []
        self.getMeaning(word)

    def getMeaning(self, word):
        word = word.encode("utf-8")
        urlParams = {}
        urlParams['key'] = properties['key']
        urlParams['lang_from'] = 'tr'
        urlParams['query'] = word
        urlValues = urllib.urlencode(urlParams)
        fullUrl = "http://api.seslisozluk.com/?" + urlValues
        req = urllib2.Request(fullUrl, None, {'Content-Type': 'application/json'})
        opener = urllib2.build_opener()
        f = opener.open(req)
        jData = f.read()
        jData = self.cleanTags(jData)
        jsondata = json.loads(jData)
        self.jsondata = jsondata

    def cleanTags(self, data):
        p = re.compile(r'<script(.*)>(.*)</script>',flags=re.S)
        return p.sub('', data)

    def create_meaning_list(self):
        allMeanings = self.jsondata['translations']
        for mean in allMeanings:
            if (mean['lang_pair'] == 'tr-en'):
                self.englishMeanings.append(mean['translation'])
            elif(mean['lang_pair'] == 'tr-tr'):
                self.turkishMeanings.append(mean['translation'])
        
    
    def prettyPrinter(self, data):
        pp = pprint.PrettyPrinter()
        pp.pprint(data)
        
