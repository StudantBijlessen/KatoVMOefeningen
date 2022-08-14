with open('input.txt', 'r') as input_file:
    with open('output.txt', 'w+') as output_file:
        content = input_file.read().splitlines()
        for line in content:
            number= int(line)
            binair= bin(number)[2:]
            output_file.write(f'{binair}\n')

    