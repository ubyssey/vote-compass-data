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

num_questions=[]

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

print(num_questions)




