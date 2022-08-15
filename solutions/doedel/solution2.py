import csv
from functools import cmp_to_key


def compare_dates(item1, item2):
    return item2['count'] - item1['count']


def main():
    with open('input.csv', 'r') as input_file:
        input_file_csv_reader = csv.reader(input_file)

        header = next(input_file_csv_reader)
        print(header)

        dates = []

        for date in header[1:]:
            dates.append({
                "datum": date,
                "count": 0
            })

        for row in input_file_csv_reader:
            # eerste getal => inclusief
            # tweede getal => exclusief
            for i in range(1, len(row)):
                if row[i] == 'yes':
                    dates[i - 1]['count'] += 1

        sorted_dates = sorted(dates, key=cmp_to_key(lambda item1, item2: item2['count'] - item1['count']))

        with open('output.txt', 'w+') as output_file:
            for date in sorted_dates:
                output_file.write(f'{date["datum"]} {date["count"]}\n')

    pass


main()
