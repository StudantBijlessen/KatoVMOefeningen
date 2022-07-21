import csv


def calculate_fine(speed: int) -> int:
    if speed <= 120:
        return 0

    return speed - 120


def write_output(fines):
    sorted_fines = sorted(fines.items(), key=lambda x: (x[1], x[0]))
    print(sorted_fines)

    with open('output.txt', 'w') as output_file:
        for fine in sorted_fines:
            output_file.write(f'{fine[0]}: {fine[1]}\n')


def main():
    violation_fines = {}

    with open("violations.csv") as input_file:
        input_dict = csv.DictReader(input_file)
        for violation in input_dict:

            fine = calculate_fine(int(violation['speed']))

            if violation['license_plate'] in violation_fines:
                violation_fines[violation['license_plate']] += fine
            else:
                violation_fines[violation['license_plate']] = fine

        write_output(violation_fines)


if __name__ == '__main__':
    main()
