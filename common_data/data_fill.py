from random import choices

from db import db
from db.work_functions import purchase, supply, top_up_balance
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

def make_job():
    purchasers = choices([i for i in db.purchasers.find()], k=5)
    providers = choices([i for i in db.providers.find()], k=4)
    products = choices([i for i in db.products.find()], k=4)

    top_up_balance(purchasers[0].get('_id'), '1337.4')
    supply(providers[0].get('_id'), products[0].get('_id'), '14')
    purchase(purchasers[1].get('_id'), products[0].get('_id'), '44')

    top_up_balance(purchasers[1].get('_id'), '228.2')
    supply(providers[1].get('_id'), products[0].get('_id'), '33')
    top_up_balance(purchasers[2].get('_id'), '5555.1')

    purchase(purchasers[2].get('_id'), products[2].get('_id'), '43')
    supply(providers[2].get('_id'), products[1].get('_id'), '1')
    supply(providers[3].get('_id'), products[2].get('_id'), '14')

    purchase(purchasers[0].get('_id'), products[0].get('_id'), '44')
    top_up_balance(purchasers[2].get('_id'), '111.15')
    purchase(purchasers[4].get('_id'), products[2].get('_id'), '12')

    purchase(purchasers[3].get('_id'), products[3].get('_id'), '12')
    top_up_balance(purchasers[3].get('_id'), '14.11')
    top_up_balance(purchasers[4].get('_id'), '122.1')
    