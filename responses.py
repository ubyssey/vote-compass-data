import csv
from datetime import datetime

def get_responses_as_list():
    with open('responses.csv') as csv_file:

        reader = csv.reader(csv_file)

        # Skip the header row
        next(reader)

        return list(reader)

responses = get_responses_as_list()

def before_cutoff_date(date):

    cutoff_date = datetime(2017, 3, 10, 17)

    response_date = datetime.strptime(date, '%m/%d/%Y %H:%M:%S')

    return response_date < cutoff_date

def num_skipped(answers):
    return len(filter(lambda x: x == '', answers))

def is_valid_response(row):
    return num_skipped(row[1:]) < 10 and before_cutoff_date(row[0])

print len(responses)

responses = filter(is_valid_response, responses)

print len(responses)
