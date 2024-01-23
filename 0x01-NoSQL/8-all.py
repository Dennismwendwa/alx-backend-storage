#!/usr/bin/env python3
"""This script list all documents in mongo db collection"""


def list_all(mongo_collection):
    """Listing all documments in mongo collection"""
    return [document for document in mongo_collection.find()]
