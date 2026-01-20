import csv

def read_csv(filename):
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  
        data = list(reader)
    return data

print(read_csv('base.csv'))