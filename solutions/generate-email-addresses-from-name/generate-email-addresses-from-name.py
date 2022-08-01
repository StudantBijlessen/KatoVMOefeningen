with open('input.txt') as f:
    with open('output.txt', 'w') as out:
        for line in f:
            name = line.strip()
            parts = name.split(' ')
            firstname = parts[0].lower()
            lastname = ''.join(parts[1:]).lower()
            domain = 'student.ucll.be'
            print(f'{firstname}.{lastname}@{domain}', file=out)