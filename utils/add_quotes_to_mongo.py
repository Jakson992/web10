import json
from bson.objectid import ObjectId

from pymongo import MongoClient

client = MongoClient('mongodb+srv://djangoWeb10:567234@cluster0.plizfca.mongodb.net/?retryWrites=true&w=majority')

db = client.django

with open('quotes.json', 'r', encoding='utf-8') as fd:
    quotes = json.load(fd)

for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
        db.quotes.insert_one({
            'quote': quote['text'],
            'tags': quote['tags'],
            'author': ObjectId(author['_id'])
        })
