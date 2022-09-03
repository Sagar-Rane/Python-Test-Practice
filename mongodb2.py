import pymongo
client = pymongo.MongoClient("mongodb+srv://sagar:sagar1234@mongo-cluster.inx6mzk.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['inventory']
collection = database['table']

data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]

# collection.insert_many(data)

print(' print all data ')

a = collection.find()
for i in a:
    print(i)

print(' print for status A ')

d = collection.find({'status': 'A'})
for i in d:
    print(i)

print(' print for status A or P')

d1 = collection.find({'status':{'$in' :['A','P']}})
for i in d1:
    print(i)

print(' print for status greater  than C')

d2 = collection.find({'status':{'$gt' :'C'}})
for i in d2:
    print(i)

print(' print for quantity greater than 50')

d3 = collection.find({'qty':{'$gt' :50}})
for i in d3:
    print(i)

print(' print for quantity greater than 50 AND item is sketch pad')

d4 = collection.find({'item':'sketch pad','qty':{'$gt' :50}})
for i in d4:
    print(i)

print(' print for quantity greater than 50 OR item is sketch pad')

d5 = collection.find({'$or' :[{'item':'sketch pad'},{'qty':{'$gte' :50}}]})
for i in d5:
    print(i)

print(' print for update item')

#collection.update_one({'item': 'canvas'},{'$set':{'item':'canvas board'}})

print(' print for delete item')

#collection.delete_one({'item':'canvas board'})