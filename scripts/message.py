import smtplib
import os

def generate_message(missing_list, sender, sender_email, receiver_email, subject):
    file_errors = ''
    
    for e in missing_list:
        file_errors += f"{e['new_path']}\n"
        file_errors += f"{e['error_message']}\n\n"
        
    message = f"""From: {sender} <{sender_email}>
To: <{receiver_email}>
Subject: {subject}

{file_errors}
"""
    
    return message

def send_email(missing_list):
    # Get the current dir of the script file and load environmental variables
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    sender = 'Tapis Project'
    sender_email = 'noreply@tapis-project.org'
    receiver_email = os.environ.get('RECEIVER_EMAIL')
    subject = os.environ.get('EMAIL_SUBJECT')
    message = generate_message(missing_list, sender, sender_email, receiver_email, subject)
    
    try:
       smtpObj = smtplib.SMTP('smtp.hawaii.edu', 25, timeout=5)
       smtpObj.sendmail(sender_email, receiver_email, message)         
       print("Successfully sent email")
    except smtplib.SMTPException as e:
       print("Error: unable to send email", str(e))