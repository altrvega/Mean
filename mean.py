#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.file_reader import *
from utils.translator import *
from utils.wordnet import *

class Mean(object):
    """
    """
    
    def __init__(self):
        """
        """
        word_list = FileReader.get_word_list()
        for word in word_list:
            word  = word.strip()
            meaning_list = self.get_meaning_list(word)
            synset_list = self.get_synset_list(meaning_list)
            print synset_list
            

    def get_meaning_list(self, word):
        trObj = Translator(word)
        trObj.create_meaning_list()
        #print trObj.englishMeanings
        return trObj.englishMeanings

    def get_synset_list(self, meaning_list):
        synset_list = []
        for meaning in meaning_list:
            temp_list = WordnetProcess.getSynsets(meaning, pos='NOUN', limit=3)
            for synset in temp_list:
                synset_list.append(synset)
        return synset_list


if __name__ == '__main__':
    mean = Mean()
        
        

