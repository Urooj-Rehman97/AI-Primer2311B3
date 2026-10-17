from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')   #MongoClient use for connection

db = client["PyDatabase"] #Database
collection = db["user"]

# if(client):
#     print("Database Connected Successfully")

#Insert/Create
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    password = input("Enter Your Password: ")
    singleUser = {
        "name": name,
        "email": email,
        "password": password
    }

collection.insert_one(singleUser)


# Read / Fetch
data = collection.find()

print("------------------- Our Users Details")
for d in data:
    print(d)

#update
    collection.update_many({"name": "Urooj Rehman"},
    {"$set": {"email": "uroojrehman@gmail.com"}})


#delete
deletedUser = collection.delete_many({"name": "Xyz"})
print("\n----------------- Deleted User --------------\n")
print(deletedUser)
