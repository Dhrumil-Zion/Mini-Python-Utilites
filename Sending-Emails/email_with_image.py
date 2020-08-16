# before sending email you have to enable your less secure apps access in your sending mail (xyz@gmail.com)

import smtplib
import imghdr
from email.message import EmailMessage

# multiple_emails = ['xyz.com', 'pqr@gmail.com']   # multiple email-id's to send at goes here

EMAIL_ADDRESS = "xyz@gmail.com"                     # your email-id goes here
EMAIL_PASSWORD = "xyz"                              # your password goes here

msg = EmailMessage()
msg['Subject'] = 'this is subject'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS

# msg['To'] = multiple_emails                       # if multiple emails are to be sent plzz uncomment this line

msg.set_content('Content area')                     # images names and relative path goes here

images = ['1.png', '2.png']

for file in images:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)
