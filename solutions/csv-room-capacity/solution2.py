import csv


def calculate_max_occupancy(examenmomenten_dict: dict) -> int:
    return max(examenmomenten_dict.values())


def main():
    exam_schedule = dict()

    with open('exam-schedule.csv', 'r') as input_file:
        exam_schedule_reader = csv.reader(input_file)
        header = next(exam_schedule_reader)

        for row in exam_schedule_reader:
            lokaal = row[12]
            examenmoment = f'{row[3]} {row[5]}'
            print(f'{examenmoment} {lokaal}')

            if lokaal not in exam_schedule:
                exam_schedule[lokaal] = dict()

            if examenmoment not in exam_schedule[lokaal]:
                exam_schedule[lokaal][examenmoment] = 1
            else:
                exam_schedule[lokaal][examenmoment] += 1

    exam_schedule_max_occupancies = {k: calculate_max_occupancy(v) for k, v in exam_schedule.items()}

    with open('output.txt', 'w+') as output_file:
        for lokaal, aantal in sorted(exam_schedule_max_occupancies.items()):
            output_file.write(f'{lokaal} {aantal}\n')


main()
