#!/usr/bin/python3
"""models/base.py"""
import json
import os


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        json_string = json.dumps(list_dictionaries)
        if list_dictionaries is None:
            return "[]"
        else:
            return json_string

    @classmethod
    def save_to_file(cls, list_objs):
        filname = f"{cls.__name__}.json"
        new_list = []
        if list_objs:
            for i in list_objs:
                new_list.append(cls.to_dictionary(i))
        json_str = cls.to_json_string(new_list)

        with open(filname, "w", encoding='utf-8') as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):

        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy_istance = cls(1, 1)
        else:
            dummy_istance = cls(1)
        dummy_istance.update(**dictionary)
        return dummy_istance

    @classmethod
    def load_from_file(cls):
        filename = f"{cls.__name__}.json"
        new_list = []
        if os.path.isfile(filename):
            with open(filename, "r", encoding='utf-8') as file:
                data = cls.from_json_string(file.read())
            for i in data:
                new_list.append(cls.create(**i))
        return new_list
