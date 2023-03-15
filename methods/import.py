""" example code for the references app"""
import os
import django
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from config.models import *

with open('../files/methods.csv', newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter=',', quotechar='"')

    # loop over each row to add to database
    for row in rows:
        if row[0] == 'code':
            continue

        # assign variables to row headers
        vcode = row[0]
        vperr = row[1]
        vsupp = row[2]
        vserj = row[3]

        # create new Methods class and set variables as row values
        methods = Methods(code=vcode, perrin=vperr, perrinsupp=vsupp, serjeant=vserj)

        # save methods data into database (per row)
        methods.save()

        # print ingest for each row to confirm
        print('row' + vcode + ' ingested')

        exit()




    for row in rows:
        # ignore the first line which is the column names
        if row[0] == 'code':
            continue
        vcode = row[0]
        vperr = row[1]
        vsupp = row[2]
        vserj = row[3]
        m = Methods(code=vcode, perrin=vperr, perrinsupp=vsupp, serjeant=vserj)
        m.save()
        print('row ' + vcode + ' ingested')
