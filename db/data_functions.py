from prettytable import PrettyTable

from db import db


def supplies_and_purchases():
    supplies = db.supplies.find()
    result = PrettyTable(('Name', 'Provider or Purchaser', 'Time', 'Amount', 'Price'))
    for i in supplies:
        product = db.products.find_one({"_id": i.get('product_id')})
        provider = db.providers.find_one({"_id": i.get('provider_id')})
        result.add_row([
            product.get('name'),
            provider.get('name'),
            i.get('time'),
            i.get('amount'),
            -product.get('price') * i.get('amount')
        ])
    purchases = db.purchases.find()
    for i in purchases:
        product = db.products.find_one({"_id": i.get('product_id')})
        purhcaser = db.purchasers.find_one({"_id": i.get('purchaser_id')})
        result.add_row([
            product.get('name'),
            f"{purhcaser.get('surname')} {purhcaser.get('firstName')}",
            i.get('time'),
            i.get('amount'),
            product.get('price') * i.get('amount')
        ])
    print(result)

def rating():
    result = PrettyTable(('Name', 'Purchases sum', 'Purchasers amount', 'Purchases amount'))
    purchases = db.purchases.find()
    pre_res = {}
    for i in purchases:
        product = db.products.find_one({"_id": i.get('product_id')})
        if not pre_res.get(product.get('name')) is None:
            pre_res[product.get('name')]['Purchases sum'] += i.get('amount') * product.get('price')
            pre_res[product.get('name')]['Purchasers amount'] += 1
            pre_res[product.get('name')]['Purchases amount'] += i.get('amount')
        else:
            pre_res[product.get('name')] = {}
            pre_res[product.get('name')]['Purchases sum'] = i.get('amount') * product.get('price')
            pre_res[product.get('name')]['Purchasers amount'] = 1
            pre_res[product.get('name')]['Purchases amount'] = i.get('amount')
    for i in pre_res.items():
        result.add_row((i[0], i[1]['Purchases sum'], i[1]['Purchasers amount'], i[1]['Purchases amount']))
    print(result)