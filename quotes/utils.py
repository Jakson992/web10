from pymongo import MongoClient


def get_mongodb():
    client = MongoClient('mongodb+srv://djangoWeb10:567234@cluster0.plizfca.mongodb.net/?retryWrites=true&w=majority')

    db = client.django
    return db
