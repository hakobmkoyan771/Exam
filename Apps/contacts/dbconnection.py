#!/usr/bin/python3
import pymongo
import os

connectionString = "mongodb://{}:27017".format(os.getenv('MONGO_DB_IP_ADDRESS'))

# The IP address should be Bridge IP or network gateway IP address see more in README.md
client = pymongo.MongoClient(str(connectionString))

database = client['project']
user_collection = database['users']


def match_email(email):
    matching_mail = user_collection.find_one({"mail": email})
    print(matching_mail)
    return matching_mail


def register_user(email, name, surname):
    user_collection.insert_one(
        {"mail": email, "name": name, "surname": surname})


def read_users():
    users_list = []
    users_data = user_collection.find({})
    for el in users_data:
        users_list.append(el)
    return users_list
