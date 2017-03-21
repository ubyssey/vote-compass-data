import csv
from datetime import datetime

def get_responses_as_list():
    with open('responses.csv') as csv_file:

        reader = csv.reader(csv_file)

        return list(reader)

responses = get_responses_as_list()

def before_cutoff_date(date):

    cutoff_date = datetime(2017, 3, 10, 17)

    response_date = datetime.strptime(date, '%m/%d/%Y %H:%M:%S')

    return response_date < cutoff_date

def num_skipped(answers):
    return len(list(filter(lambda x: x == '', answers)))

def is_valid_response(row):
    return num_skipped(row[1:]) < 10 and before_cutoff_date(row[0])

print (len(responses))

questions = responses[0][1:]

responses = list(filter(is_valid_response, responses[1:]))

print (len(responses))

num_questions = []

for i, q in enumerate(questions):

    totals = {
        'Strongly Agree': 0,
        'Agree': 0,
        'Neutral': 0,
        'Disagree': 0,
        'Strongly Disagree': 0
    }

    for response in responses:

        answer = response[i+1]

        if answer:
            totals[answer] += 1

    num_questions.append(totals)

def get_total(totals, response):
    return [total[response] for total in totals]

with open('totals.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file)

    writer.writerow(['Response'] + questions)

    writer.writerow(['Strongly Agree'] + get_total(num_questions, 'Strongly Agree'))
    writer.writerow(['Agree'] + get_total(num_questions, 'Agree'))
    writer.writerow(['Neutral'] + get_total(num_questions, 'Neutral'))
    writer.writerow(['Disagree'] + get_total(num_questions, 'Disagree'))
    writer.writerow(['Strongly Disagree'] + get_total(num_questions, 'Strongly Disagree'))

print(num_questions)
