from json import loads

from bson.objectid import ObjectId

from db import db
from db.utils import collection_check


@collection_check
def insert_from_file(collection: str, file_path: str):
    with open(file_path, 'r') as f:
        for i in loads(f.read())[collection]:
            i['_id'] = str(ObjectId())
            db[collection].insert_one(i)
            print(f"Object {i}, inserted into {collection}")

@collection_check
def change(collection: str, id: str, item: str, new_value: str):
    if db[collection].update_one({'_id': id}, {'$set': {item: new_value}}).raw_result.get('updatedExisting'):
        print(f"Object {db[collection].find_one({'_id': id})} from {collection} was successfully updated")
    else:
        print(f"There's no such object in {collection}")

@collection_check
def delete(collection: str, id: str):
    if db[collection].delete_one({'_id': id}).deleted_count:
        print(f"Object {db[collection].find_one({'_id': id})} was successfully deleted from {collection}")
    else:
        print(f"There's no such object in {collection}")
