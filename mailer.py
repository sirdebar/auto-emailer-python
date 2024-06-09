import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# example secret pass for mail.ru(spam abuse)
PASSWORD = "Fk8HYwqqkC5vztYeczvq" 

#email sender func
def send_email(from_address, to_address, subject, message):
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.mail.ru', 587)
        server.starttls()
        server.login(from_address, PASSWORD)
        server.sendmail(from_address, to_address, msg.as_string())
        server.quit()
        print(f"Email sent to {to_address} from {from_address}")
    except Exception as e:
        print(f"Failed to send email to {to_address} from {from_address}: {e}")

# database connect
conn = sqlite3.connect('email_sender.db')
cursor = conn.cursor()

# get all accounts
cursor.execute('SELECT email FROM email_accounts WHERE email LIKE "%@mail.ru"')
email_accounts = cursor.fetchall()

# get all senders
cursor.execute('SELECT email FROM recipients')
recipients = cursor.fetchall()

# database kill connect
conn.close()

# theme and message
subject = "Hello"
message = "Privet"

# sender
for account in email_accounts:
    from_address = account[0]
    for recipient in recipients:
        to_address = recipient[0]
        send_email(from_address, to_address, subject, message)
