from email.mime.text import MIMEText
import smtplib
import secrets

def send_email(email, height, average_height, count):
    from_email = 'nantog@gmail.com'
    from_password = secrets.gmail_password
    to_email = email

    subject = 'height data'
    message = 'Hey there, your height is <b>{}</b><br>' \
              'Average height of all is <b>{}</b><br>' \
              'Number of people is <b>{}</b>'.format(height, average_height, count)

    msg = MIMEText(message, 'html')

    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)


