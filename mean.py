#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.file_reader import *
from utils.translator import *

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
            

    def get_meaning_list(self, word):
        trObj = Translator(word)
        trObj.create_meaning_list()
        print trObj.englishMeanings
        return trObj.englishMeanings


if __name__ == '__main__':
    mean = Mean()
        
        

