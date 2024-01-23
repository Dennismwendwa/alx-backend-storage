#!/usr/bin/env python3
"""This script updates all topics of document"""


def update_topics(mongo_collection, name, topics):
    """Updating all documments"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}},
    )
