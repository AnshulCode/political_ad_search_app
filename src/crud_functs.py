import pymongo
from json import dumps
from json import loads

client = pymongo.MongoClient("mongodb://localhost:27017/")
dbs = client["poli_db"]
restDB = dbs["dbs"]


a = restDB.find({})


def create(org):
    return
def find(org):
    list = []
    obj = restDB.find({"organization":org})
    for i in obj:
       id = i["_id"]
       ids = str(id)
       i["_id"] = ids
       list.append(i)
    json = dumps(list)
    return json
def delete(message):
    obj = restDB.find_one({"message": message})
    restDB.delete_one(obj)
    return
def update(id,message):
    list = []
    obj = restDB.find_one({"_id":id})
    obj["message"] = message
    return obj
