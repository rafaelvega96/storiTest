
import json
import pymongo

def insert(data):
    print("Insert in mongoDB")
    try:
        # write item to database
        collection = connectionDB()
        collection.insert_one(data)
    except NameError as e:
        print(e)


def connectionDB():
    client = pymongo.MongoClient(
        "mongodb+srv://rafaelvega96:vega190896@cluster0.riesk.mongodb.net/?retryWrites=true&w=majority")
    db = client["stori"]
    return db["accounts_transactions"]