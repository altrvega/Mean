#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nltk.corpus import wordnet as wn
        
class WordnetProcess:

    
    @staticmethod    
    def getSynsets(*args, **kwargs):
        """pos ile turunu veriyoruz
        limit ile kac tane synset alabileceimizi belirleyebiliyoruz
        """
        if ('pos' in kwargs):
            pos = kwargs['pos']
            if (pos == 'NOUN'):
                synsetsList = wn.synsets(args[0], pos=wn.NOUN)
            elif (pos == 'VERB'):
                synsetsList = wn.synsets(args[0], pos=wn.VERB)
            elif (pos == 'ADV'):
                synsetsList = wn.synsets(args[0], pos=wn.ADV)
            elif (pos == 'ADJ'):
                synsetsList = wn.synsets(args[0], pos=wn.ADJ)
            elif (pos == 'ALL'):
                synsetsList = wn.synsets(args[0])
            else:
                synsetsList = wn.synsets(args[0])
        else:
            synsetsList = wn.synsets(args[0])
            
        if ('limit' in kwargs):
            limit = kwargs['limit']
            synsetsList = WordnetProcess.getSubList(synsetsList, limit)
            
        return synsetsList

    @staticmethod
    def getSubList(list, pieces):
        newlist = []
        counter = 0
        for l in list:
            if (counter < pieces):
                newlist.append(l)
                counter = counter + 1
            else :
                break
        return newlist

    
    #  using Wu-palmer algorithm
    @staticmethod
    def getSimilarity(synsetOne, synsetTwo):
        val = synsetOne.wup_similarity(synsetTwo)
        return val

    @staticmethod
    def getHypernyms(synset):
        return synset.hypernyms()
