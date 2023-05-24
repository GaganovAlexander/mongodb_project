from db import db
from db.data_manipulation import insert_from_file


def init_db():
    db.providers.delete_many({})
    db.purchasers.delete_many({})
    db.products.delete_many({})
    db.supplies.delete_many({})
    db.purchases.delete_many({})
    insert_from_file('providers', './common_data/providers.json')
    insert_from_file('products', './common_data/products.json')
    insert_from_file('purchasers', './common_data/purchasers.json')