# -*- coding:utf-8 -*-
import datetime
from pymongo import MongoClient
client = MongoClient("mongodb://admin:adminpw@127.0.0.1:27017")

db = client.pythondb

post = {"author": "Maxsu",
         "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print ("post id is ", post_id)