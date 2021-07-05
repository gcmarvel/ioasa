import datetime
from datetime import timedelta
import csv


with open('catalogue_data.csv', 'r') as cat_data:
    data_reader = csv.DictReader(cat_data)
    data = []
    for line in data_reader:
        data.append({'starid': line['starid'], 'name': line['name'], 'country': line['country'], 'magnitude': line['magnitude'], 'constellation': line['constellation'], 'date': datetime.datetime.strptime(line['date'], '%Y-%m-%d').date(), })

new_data = [x for x in data if x['date'] <= (datetime.date.today())]