from pymongo import MongoClient


def get_mongodb():
    client = MongoClient("mongodb://localhost")
    db = client.hw
    return db
# def get_postgres():
#     client = MongoClient("mongodb://localhost")
#     db = client.hw
#     return db