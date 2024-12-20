import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import string

def generate_random_string(length=5):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def send_email(sender_email, sender_password, recipient_email, subject, message):
    smtp_server = "smtp.gmail.com"  
    smtp_port = 587  

    email_body = MIMEText(message, "plain")

    email_message = MIMEMultipart()
    email_message["From"] = sender_email
    email_message["To"] = recipient_email
    email_message["Subject"] = subject

    email_message.attach(email_body)

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  

    server.login(sender_email, sender_password)


    server.sendmail(sender_email, recipient_email, email_message.as_string())


    server.quit()

sender_email="pradheeban.a2022ai-ml@sece.ac.in"
sender_password = "veluanand"
recipient_email = "topuprip@gmail.com"
subject = "Test Email "  
message ="This is your Code for Joining in the call :"+ generate_random_string()

send_email(sender_email, sender_password, recipient_email, subject, message)