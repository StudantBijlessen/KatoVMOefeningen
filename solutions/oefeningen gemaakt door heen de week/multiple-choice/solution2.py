import csv
rows_answers = []
rows_solution = []
with open('answers.csv', 'r') as answerfile:
    with open('solutions.csv', 'r') as solutionsfile:
        solutions = solutionsfile.read().strip().split(',')
        csvreader_answerfile = csv.reader(answerfile)
        for row in csvreader_answerfile:
            rows_answers.append(row)
        
        for data in rows_answers:
            print((data[0]))

        




