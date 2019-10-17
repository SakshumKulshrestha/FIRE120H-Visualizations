import csv
import pandas as pd

codes_file = pd.read_csv("Data Files\plotly_countries_and_codes.csv")
data_file = pd.read_csv("Data Files\\2017_trust_in_gov.csv")

data_file['CODE'] = codes_file['CODE']

data_file.to_csv('file_with_codes.csv', index=False)
