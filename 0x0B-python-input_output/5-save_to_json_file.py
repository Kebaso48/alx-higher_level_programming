#!/usr/bin/python3
"""DEfines a JSON writing function"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a file using JSON rpresentation"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
