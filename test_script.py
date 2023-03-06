import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def print_head(data, n):
    return data.head(n)

file_path = "annual-enterprise-survey-2021-financial-year-provisional-csv.csv"

data = load_data(file_path)

print(print_head(data, 20))