#!/usr/bin/env python3
"""This script insert a document in a collection"""


def insert_school(mongo_collection, **kwargs):
    """Inserting document in collection"""
    collection = mongo_collection.insert_one(kwargs)
    return collection.inserted_id
