#!/usr/bin/env python3
"""Task 12"""
from pymongo import MongoClient


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
stats = """{} logs
Methods:
    method GET: {}
    method POST: {}
    method PUT: {}
    method PATCH: {}
    method DELETE: {}
{} status check""".format(logsCount, getCount,
                          postCount, putCount,
                          patchCount, deletCount,
                          checkCount)
print(stats)
