import pymongo
client = pymongo.MongoClient("mongodb+srv://sagar:sagar1234@mongo-cluster.inx6mzk.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    'name':'sagar',
    'email':'sagar@gmail.com',
    'surname':'rane'
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)


