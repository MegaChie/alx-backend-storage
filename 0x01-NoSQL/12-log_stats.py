#!/usr/bin/env python3
"""Task 12"""
from pymongo import MongoClient


def statsView():
    """Prints statistics about the database"""
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    colct = db.nginx
    logsCount = colct.count_documents({})
    getCount = colct.count_documents({"method": "GET"})
    postCount = colct.count_documents({"method": "POST"})
    putCount = colct.count_documents({"method": "PUT"})
    patchCount = colct.count_documents({"method": "PATCH"})
    deletCount = colct.count_documents({"method": "DELETE"})
    checkCount = colct.count_documents({"method": "GET", "path": "/status"})
    print("{} logs".format(logsCount))
    print("Methods:")
    print("\tmethod GET: {}".format(getCount))
    print("\tmethod POST: {}".format(postCount))
    print("\tmethod PUT: {}".format(putCount))
    print("\tmethod PATCH: {}".format(patchCount))
    print("\tmethod DELETE: {}".format(deletCount))
    print("{} status check".format(checkCount))


if __name__ == "__main__":
    statsView()
