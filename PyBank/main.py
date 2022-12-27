import csv
import os

path = 'Resources/budget_data.csv'

with open(path) as csvfile:
    reader = path.reader(csvfile)
    print(reader)
    
