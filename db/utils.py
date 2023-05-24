from db import db


def collection_check(func):
    def wrapper(collection, *args, **kwargs):
        if not collection in db.list_collection_names():
            print(f"collection {collection} does not exists")
            return
        return func(collection, *args, **kwargs)
    return wrapper