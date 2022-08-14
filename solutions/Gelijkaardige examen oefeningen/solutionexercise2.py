import json


def bereken_totaal(items: list, catalogus: dict) -> float:
    totaal = 0

    for item in items:
        totaal += catalogus[item]

    return totaal


def main():
    creditcard_total = dict()
    catalog = None

    with open('catalog.json', 'r') as catalog_file:
        catalog = json.load(catalog_file)

    with open('orders.json', 'r') as orders_file:
        # Niet tweede file al open doen
        orders = json.load(orders_file)

        for order in orders:
            creditcard_total[order["credit_card"]] = bereken_totaal(order["items"], catalog)


main()
