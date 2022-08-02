import re


def replace_headers(match):
    catched_string = match.group(1)
    return catched_string.replace('#', '=')


def replace_indentations(match):
    catched_string = match.group()

    return catched_string.replace('  ', '*')


def main():
    with open('input.md', 'r') as input_file:
        content = input_file.read()

        content_headers_replaced = re.sub(r"^(#*)", replace_headers, content, flags=re.M)
        content_headers_indentations_replaced = re.sub(r"^(( {2})+)\*", replace_indentations, content_headers_replaced,
                                                       flags=re.M)
        with open('output.txt', 'w+') as output_file:
            output_file.write(content_headers_indentations_replaced)


main()
