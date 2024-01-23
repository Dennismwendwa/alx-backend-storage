#!/usr/bin/env python3
"""This script returns the documents with a martch"""


def schools_by_topic(mongo_collection, topic):
    """Listing all school with the given topic"""
    my_topics = {
        "topics": {
            "$elemMatch": {
                "$eq": topic,
            },
        },
    }

    return [document for document in mongo_collection.find(my_topics)]
