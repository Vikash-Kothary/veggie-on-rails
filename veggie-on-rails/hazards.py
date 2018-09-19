#!/usr/bin/venv python3
"""
hazards.py - Classifying if vegetation is consider as a hazard
"""

#from utils import clean_json
import json


def main():
    with open("data/frames.json", "r") as read_file:
        data = json.load(read_file)
    #print(json.dumps(data, indent=4, sort_keys=True))


if __name__ == '__main__':
    main()
