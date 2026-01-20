from read_csv import read_csv
from send_mail import send_mail
from write_csv import write_csv
def process_and_send(csv_file):
    rows = read_csv(csv_file)

    for row in rows:
        send_mail(row,csv_file,rows.index(row))

        # mailer.send(email)

        print(f"Sent mail to {row[4]} | {row[5]}")

