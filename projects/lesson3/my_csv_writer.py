import get_answers
import csv


new_answers = []
for key in get_answers.answers:
    new_answers.append(dict(zip(['question', 'answer'], [key, get_answers.answers[key]])))

with open('new_answers.csv', 'w', encoding='UTF-8') as f:
    fields = ['question', 'answer']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    writer.writerows(new_answers)