#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.file_operations import *
from utils.translator import *
from utils.wordnet import *

class Mean(object):
    """
    """
    
    def __init__(self):
        """
        """
        word_list = FileOperations.get_word_list()
        for word in word_list:
            word  = word.strip()
            meaning_list = self.get_meaning_list(word)
            synset_list = self.get_synset_list(meaning_list)
            synset_description_list = []
            i = 1
            for synset in synset_list:
                synset_description = self.prepare_synset_description(synset, i)
                synset_description_list.append(synset_description)
                i = i + 1
            FileOperations.write_list_to_file(synset_description_list, word)
                

    def prepare_synset_description(self, synset, idx):
        hypernyms = WordnetProcess.getHypernym(synset)
        if (hypernyms): 
            hypernyms2 = WordnetProcess.getHypernym(hypernyms[0])
            if not hypernyms2:
                hypernyms2 = ['']
        else:
            hypernyms  =  ['']
            hypernyms2  = ['']

        text = str(idx) + ' ' + str(synset) + ': ' + str(synset.definition) + ' | ' + str(hypernyms[0]) + '=>' + str(hypernyms2[0]) + '...'
        return text
        
            

    def get_meaning_list(self, word):
        trObj = Translator(word)
        trObj.create_meaning_list()
        return trObj.englishMeanings

    def get_synset_list(self, meaning_list):
        synset_list = []
        for meaning in meaning_list:
            temp_list = WordnetProcess.getSynsets(meaning, pos='NOUN', limit=3)
            for synset in temp_list:
                if (synset not in synset_list):
                    synset_list.append(synset)
        return synset_list


if __name__ == '__main__':
    mean = Mean()
        
        

