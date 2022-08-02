import csv

# dict() en {} is exact hetzelfde!
id_written_exams = dict()


def main():
    rows = []

    with open('exam-schedule.csv', 'r') as input_file:
        csvreader = csv.reader(input_file)
        # Zodat volgende lijn niet meer de header bevat
        next(csvreader)

        for row in csvreader:
            rows.append(row)

    rows = [row for row in rows if row[9] == 'S']

    for row in rows:
        lecturer_ids = row[0].split('/')

        for lecturer_id in lecturer_ids:
            if lecturer_id in id_written_exams:
                id_written_exams[lecturer_id] += 1
            else:
                id_written_exams[lecturer_id] = 1

    sort_keys = id_written_exams.items()
    # to reverse order, reverse = True
    new_items = sorted(sort_keys)

    with open('output.txt', 'w+') as output_file:

        for lecturer in new_items:
            key = lecturer[0]
            value = lecturer[1]
            # output_file.write(key + " " + value + '\n')
            output_file.write(f"{key} {value}\n")

    print(new_items)


main()
print(id_written_exams)
