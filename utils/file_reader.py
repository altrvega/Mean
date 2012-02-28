#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
from properties.properties import *


class FileReader(object):
    """File Read utility
    """
    
    @staticmethod
    def get_word_list():
        """get word list from file
        """
        file_path = properties['file_dir'] + 'words.txt'
        f = io.open(file_path, 'r')
        word_list = f.readlines()
        f.close()
        return word_list

    @staticmethod
    def write_word_results(object_list):
        """write page information to a file
        not using in here
        """
        file_name = properties['search_word']
        f = io.open(properties['output_dir'] + file_name.encode('utf-8') + '.txt', 'w')
        for obj in object_list:
            line = obj._link + ' ' + obj._title + ' ' + obj._snippet + '\n'
            f.write(line)
        f.close()
        
        

        
        
