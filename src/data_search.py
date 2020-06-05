import csv
import sys
import random
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
dbs = client["poli_db"]
restDB = dbs["dbs"]
restDB.delete_many({})

csv.field_size_limit(sys.maxsize)
csvfile = open('fbpac-ads-en-US.csv')
file_reader = csv.reader(csvfile)
rows = []

paid_for_index = 21
org_index = 4
message_index = 5


i = 0
for item in file_reader:
    obj = {"organization": item[paid_for_index], "message": item[message_index]}
    print(item[paid_for_index])
    restDB.insert_one(obj)
def search(org):
    list = []
    for items in rows:
        if org.lower() == items[21].lower():
            obj = {"organization" : org, "message": items[5],"_id":random.randrange(1,1000)}
            list.append(obj)
    return list
