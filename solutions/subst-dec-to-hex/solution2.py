import re


def replace_decimal(match):
    decimal_string = match.group(1)
    uppercase = hex(int(decimal_string)).upper()
    return uppercase.replace('X', 'x')


with open('input.txt', 'r') as input_file:
    content = input_file.read()
    content_new = re.sub(r"\$HEX\((\d+)\)", replace_decimal, content, flags=re.M)

    with open('output.txt', 'w+') as output_file:
        output_file.write(content_new)
