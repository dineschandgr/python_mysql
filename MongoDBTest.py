import pymongo


connection_url = "mongodb+srv://livewirecbehopecollege:test1234@livewire.3r9b77u.mongodb.net"
client = pymongo.MongoClient(connection_url)
print(client.list_database_names())

workshop_db=client['fullstack_workshop']

collection = workshop_db['records']
print(workshop_db.list_collection_names())

documents=[{"Name":"Roshan","Roll No":159,"Branch":"CSE"},{"Name":"Rahim","Roll No":155,"Branch":"CSE"},
           {"Name":"Ronak","Roll No":156,"Branch":"CSE"}]
collection.insert_many(documents)

query={"Name":"Roshan"}
print(collection.find_one(query))

query={"Branch":"CSE"}
result=collection.find(query)
for i in result:
    print(i)

result=collection.find({}).limit(2)
for i in result:
    print("limit ",i)

query={"Roll No ":{"$eq":153}}
print(collection.find_one(query))

query={"Roll No":153}
collection.delete_one(query)