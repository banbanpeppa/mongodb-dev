# -*- coding:utf-8 -*-
import pymongo
import datetime

class MongodbConn(object):

    def __init__(self):
        self.CONN = pymongo.MongoClient("mongodb://admin:adminpw@127.0.0.1:27017")

    def run(self):
        database = "test_db"
        db = self.CONN[database]
        col = db.collection_names()[0]
        print(db.collection_names())
        collection = db.get_collection(col)
        print(collection)
        post = {"author": "Maxsu",
         "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()}
        
        posts = db.posts
        post_id = posts.insert_one(post).inserted_id
        print("post id is ", post_id)

if __name__ == '__main__':
    mo = MongodbConn()
    mo.run()