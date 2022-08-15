def main():
    with open('input.txt', 'r') as input_file:
        with open('output.txt', 'w+') as output_file:
            for line in input_file:
                name, group_2 = line.split(':')
                score_fraction, operations = group_2.split(' ')

                # Splits ook de '/'
                spent_points, earned_points = tuple(map(int, score_fraction.split('/')))

                spent_points += operations.count('-')
                earned_points += operations.count('+')
                output_file.write(f'{name}:{spent_points}/{earned_points}\n')


main()
