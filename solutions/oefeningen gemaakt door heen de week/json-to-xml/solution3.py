import json
from collections import OrderedDict

# Heel zeker dat de insertion order hetzelfde gebleven is
student_grades = OrderedDict()


def write_grades(grades):
    return "".join(f"<grade>{grade}</grade>" for grade in grades)


with open('input.json', 'r') as input_file:
    with open('output.txt', 'w+') as output_file:
        output_file.write(f'<students>\n')
        input_data = json.load(input_file)
        for student in input_data:
            id = student['id']
            grades = student['grades']
            student_grades[id] = grades

        for student, grades in student_grades.items():
            output_file.write(f'<student id="{student}"><grades>{write_grades(grades)}</grades></student>\n')
        output_file.write('</students>')
