import csv
import pandas as pd
from csv import DictReader

codes_file = pd.read_csv("Data Files\plotly_countries_and_codes.csv")
data_file = pd.read_csv("Data Files\\2017_trust_in_gov.csv")

# data_file['CODE'] = codes_file['CODE']

# data_file.to_csv('file_with_codes.csv', index=False)

#########


codes_file_location = "Data Files\\plotly_countries_and_codes.csv"
countries_file_location = "Data Files\\2017_trust_in_gov.csv"


## country_file  = csv.reader(open(countries_file_location, "rb"), delimiter=",")
## codes_file = csv.reader(open(codes_file_location, 'rb'), delimiter=",")

with open(countries_file_location, 'r') as a:
    with open(codes_file_location, 'r') as b:
        country_file = csv.reader(a)
        codes_file = csv.reader(b)

        codes = []
        next(country_file, None)

        for row in country_file:
            checker = False
            for row2 in codes_file:
                if row[0] == row2[0]:
                    checker = True
                    codes.append(row2[2])
            if(not checker):
                codes.append('NONE')
            b.seek(0)


print(codes)

data_file['CORRECT'] = codes
data_file.to_csv('new_file_correct_codes', index=False)


