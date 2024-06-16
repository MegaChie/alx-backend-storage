#!/usr/bin/env python3
"""Task 11"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specific topic"""
    seek = {"topics": topic}
    return mongo_collection.find(seek)
