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


def update_csv_with_tat(csv_path, row_index, tat_value):
    import csv

    with open(csv_path, "r", newline="") as f:
        rows = list(csv.reader(f))

    # Add header if TAT doesn't exist
    if "TAT" not in rows[0]:
        rows[0].append("TAT")

    # Append TAT to the specific row
    rows[row_index].append(tat_value)

    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
