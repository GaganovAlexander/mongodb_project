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

def turnover():
    result = PrettyTable(('name', 'supplies', 'providers', 'purchases', 'purchasers', 'profit'))
    supplies = db.supplies.find()
    purchases = db.purchases.find()
    pre_res = {i.get('_id'): {'name': i.get('name'), 'supplies': 0, 'providers': '', 'purchases': 0, 'purchasers': '', 'profit': 0} for i in db.products.find()}
    for i in supplies:
        name = db.providers.find_one({"_id": i.get('provider_id')}).get('name')
        pre_res[i.get('product_id')]['supplies'] += i.get('amount')
        pre_res[i.get('product_id')]['providers'] += ", " + name if pre_res[i.get('product_id')]['providers'] else name if name is not None else ''
        pre_res[i.get('product_id')]['profit'] -= db.products.find_one(i.get('products_id')).get('price') * i.get('amount')
    for i in purchases:
        purchaser = db.purchasers.find_one({"_id": i.get('purchaser_id')})
        name = f"{purchaser.get('surname')} {purchaser.get('firstName')}"
        pre_res[i.get('product_id')]['purchases'] += i.get('amount')
        pre_res[i.get('product_id')]['purchasers'] += ", " + name if pre_res[i.get('product_id')]['purchasers'] else name
        pre_res[i.get('product_id')]['profit'] += db.products.find_one(i.get('products_id')).get('price') * i.get('amount')
    for i in pre_res.values():
        result.add_row((i['name'], i['supplies'], i['providers'], i['purchases'], i['purchasers'], i['profit']))
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
