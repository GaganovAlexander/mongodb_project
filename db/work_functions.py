from datetime import datetime

from bson.objectid import ObjectId

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
        print(f"Successful suplie {supplie_}, new ammount = {prev_amount + amount}")
    else:
        print("Something went wrong")