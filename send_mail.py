from mailersend import MailerSendClient,EmailBuilder
from dotenv import load_dotenv
from calculate_tat import calculate_tat
from write_csv import update_csv_with_tat
from datetime import datetime

load_dotenv()

ms = MailerSendClient()



def send_mail(row,csv_path,row_index):
    interviewer_name = row[1]
    interviewer_email = row[2]
    candidate_name = row[3]
    candidate_email = row[4]
    scheduling_method = row[5]  # already ONE round
    added_on = row[6]

    subject = "Link for Calendly invite for interview call"

    body_text = f"""
Dear {candidate_name},

This is the respective link for Calendly invite for the interview call.

{scheduling_method}

Regards,
{interviewer_name}
"""

    email = (
        EmailBuilder()
        .from_email(interviewer_email, interviewer_name)
        .to_many([{"email": candidate_email, "name": candidate_name}])
        .subject(subject)
        .text(body_text)
        .build()
    )
    
    response = ms.emails.send(email)
    sent_time = datetime.now()
    tat = calculate_tat(added_on, sent_time)
    update_csv_with_tat(csv_path, row_index, tat)

    return response
