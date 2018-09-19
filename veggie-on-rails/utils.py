#!/usr/bin/venv python3
"""
utils.py - Helper functions
"""

from os import listdir
from os.path import isfile, join


def dir_files(path):
    '''
    Lists files in a directory, ignoring hidden files
    '''
    return [f for f in listdir(path) if isfile(join(path, f)) and not f.startswith('.')]
