from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")  #Database Connection

db = client["PyDatabase"]   #Database
users = db["user"]          #Collection

name = input("Enter your Name: ")
email = input("Enter Your Email: ")
password = input("Enter Your Password: ")

newUser = {
    "name" :name,
    "email": email,
    "password": password
}

users.insert_one(newUser)
print("--------------- User Register Successfully ---------------")