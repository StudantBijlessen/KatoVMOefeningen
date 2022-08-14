import re

words = {
    "A": "Aap",
    "B": "Beest",
}


def replace_text(match):
    matched_string = match.group()
    first_letter = matched_string[0]
    last_letter = matched_string[-1]
    new_word = words[first_letter]

    return f"{first_letter}{new_word}{last_letter}"


def main():
    with open('input.txt', 'r') as input_file:
        text = input_file.read()

        aangepaste_text = re.sub(r'^[ABab][^ ]{6,}[a-zA-Z]', replace_text, text, flags=re.M)

        print(aangepaste_text)


main()
