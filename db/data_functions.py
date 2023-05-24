from prettytable import PrettyTable

from db import db


def supplies_and_purchases():
    supplies = db.supplies.find()
    result = PrettyTable(('Name', 'Provider or Purchaser', 'Time', 'Amount', 'Price'))
    for i in supplies:
        product = db.products.find_one({"_id": i.get('product_id')})
        result.add_row([
            db.providers.find_one({"_id": i.get('provider_id')}).get('name'),
            product.get('name'),
            i.get('time'),
            i.get('amount'),
            -product.get('price') * i.get('amount')
        ])
    purchases = db.purchases.find()
    for i in purchases:
        product = db.products.find_one({"_id": i.get('product_id')})
        result.add_row([
            db.purchasers.find_one({"_id": i.get('purchaser_id')}).get('name'),
            product.get('name'),
            i.get('time'),
            i.get('amount'),
            product.get('price') * i.get('amount')
        ])
    print(result)
