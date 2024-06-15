#!/usr/bin/env python3
"""Task 9"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on kwargs"""
    toInsert = mongo_collection.insert_one(kwargs)
    return toInsert.inserted_id
