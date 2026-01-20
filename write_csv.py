import csv
def write_csv(filename, data):
    header = [
        'Company',
        'Interviewer',
        'Interviewer Email',
        'Candidate',
        'Candidate Email',
        'Scheduling method',
        'Added On'
    ]

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for row in data:
            scheduling_methods = row[5].split('\n')

            for method in scheduling_methods:
                new_row = [
                    row[0],  
                    row[1],  
                    row[2], 
                    row[3],
                    row[4],  
                    method.strip(),  
                    row[6]   
                ]
                writer.writerow(new_row)

