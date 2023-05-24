from datetime import datetime

from bson.objectid import ObjectId
from prettytable import PrettyTable

from db import db


def supplie(provider_id: str, product_id: str, amount: int):
    amount = float(amount)
    if amount <= 0 or amount % 1:
        print("amount should be positive integer")
        return
    amount = int(amount)
    prev_amount = db.products.find_one({"_id": product_id}).get('count')
    if db.products.update_one({"_id": product_id}, {"$inc": {"count": amount}}).raw_result.get('updatedExisting'):
        supplie_ = {"_id": str(ObjectId()), "provider_id": provider_id, "product_id": product_id, "amount": amount, "time": datetime.now()}
        db.supplies.insert_one(supplie_)
        supplie_print = PrettyTable(supplie_)
        supplie_print.add_row(supplie_.values())
        print(f"Successful suplie\n{supplie_print}\nNew ammount = {prev_amount + amount}")
    else:
        print("Something went wrong")

def purchase(purchaser_id: str, product_id: str, amount: str):
    amount = float(amount)
    if amount <= 0 or amount % 1:
        print("amount should be positive integer")
        return
    amount = int(amount)
    product = db.products.find_one({"_id": product_id}) 
    if product.get('count') < amount:
        print("Current product count leaser then purchase amount")
        return
    if db.purchasers.find_one({"_id": purchaser_id}).get('currentBalance') < amount * product.get('price'):
        print("Current purchaser balance leaser then purchase price")
        return
    if (db.products.update_one({"_id": product_id}, {"$inc": {"count": amount}}).raw_result.get('updatedExisting') and
        db.purchasers.update_one({"_id": purchaser_id}, {"$inc": {"currentBalance": -product.get('price')}}).raw_result.get('updatedExisting')):
        purchase = {"_id": str(ObjectId()), "purchaser_id": purchaser_id, "product_id": product_id, "amount": amount, "time": datetime.now()}
        db.purchases.insert_one(purchase)
        purchase_print = PrettyTable(purchase)
        purchase_print.add_row(purchase.values())
        print(f"Successful suplie\n{purchase_print}\nPurchase price = {amount * product.get('price')}")
    else:
        print("Something went wrong")