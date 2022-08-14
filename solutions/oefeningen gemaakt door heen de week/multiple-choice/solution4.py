import csv
from collections import OrderedDict


def calculate_score(answers: list, solutions: list) -> int:
    score = 0
    for i in range(len(answers)):
        if answers[i] == solutions[i]:
            score += 1

    return score


def main():
    solutions = []
    answers_dictionary = OrderedDict()

    with open('solutions.csv', 'r') as solutions_file:
        # Strip gebruikt voor de zekerheid
        solutions = solutions_file.read().strip().split(",")

    with open('answers.csv', 'r') as answer_file:
        answers_csv_reader = csv.reader(answer_file)
        for row in answers_csv_reader:
            name = row[0]
            answers = row[1:]
            answers_dictionary[name] = calculate_score(answers, solutions)

    with open('output.txt', 'w+') as output_file:
        for person in answers_dictionary.items():
            output_file.write(f"{person[0]} {person[1]} \n")


main()
