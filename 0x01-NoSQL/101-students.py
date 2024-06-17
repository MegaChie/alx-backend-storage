#!/usr/bin/env python3
"""Task 14"""


def top_students(mongo_collection):
    """Returns all students sorted by average score"""
    steps = [
            {"$project": {"name": "$name",
                          "averageScore": {"$avg": "$topics.score"}
                          }
             },
            {"$sort": {"averageScore": -1}
             }
             ]
    res = mongo_collection.aggregate(steps)
    return res
