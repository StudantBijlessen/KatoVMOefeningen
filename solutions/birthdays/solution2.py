import json

# Dictionary kan gebruikt worden om values to mappen
monthnr_month = {
    1: 'januari',
    2: 'februari',
    3: 'maart',
    4: 'april',
    5: 'mei',
    6: 'juni',
    7: 'juli',
    8: 'augustus',
    9: 'september',
    10: 'oktober',
    11: 'november',
    12: 'december'
}

maanden = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0
}


def get_prefix(month_name: str):
    return " " * (10 - len(month_name))


with open('data.json', 'r') as file:
    list_of_people = json.load(file)
    # For loop: we weten op voorhand
    for person in list_of_people:
        birthday = person['birthday']
        maanden[birthday['month']] += 1

    for monthnr, freq in maanden.items():
        print(f'{get_prefix(monthnr_month[monthnr])}{monthnr_month[monthnr]}: {"*" * freq}')

    print('hi')
