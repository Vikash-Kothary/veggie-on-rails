#!/usr/bin/venv python3
"""
utils.py - Helper functions
"""

import json
from os import listdir
from os.path import isfile, join


def dir_files(path):
    '''
    Lists files in a directory, ignoring hidden files
    '''
    return [f for f in listdir(path) if isfile(join(path, f)) and not f.startswith('.')]


def clean_json():
    with open("data/reconstruction.json", "r") as read_file:
        data = json.load(read_file)
    with open('data/frames.json', 'w') as write_file:
        fields = ["camera", "capture_time", "gps_dop", "gps_position", "orientation", "rotation"]
        for frame in data[0]['shots']:
            for field in fields:
                del (data[0]['shots'][frame][field])
        json.dump(data[0]['shots'], write_file, indent=4, sort_keys=True, ensure_ascii=False)
    with open('data/points.json', 'w') as write_file:
        for point in data[0]['points']:
            del (data[0]['points'][point]["reprojection_error"])
        json.dump(data[0]['points'], write_file, indent=4, sort_keys=True, ensure_ascii=False)

    return data
