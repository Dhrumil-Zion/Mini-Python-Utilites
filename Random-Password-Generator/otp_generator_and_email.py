import random
import smtplib
from email.message import EmailMessage

otp = random.randrange(100000, 1000000)

# sirja aaya update / insert ni query marvi padse data base ma store kerva
# aya fetch karavi leje pachu tempotp variable ma
# bs pachi form mathi aaavse ane compare kari ne mail sen kerje aagad


EMAIL_ADDRESS = "shoppyapp123@gmail.com"  # your email-id goes here
EMAIL_PASSWORD = "shoppy112334556app@gmail.com"  # your password goes here

msg = EmailMessage()
msg['Subject'] = 'testing purpose'
msg['From'] = EMAIL_ADDRESS
msg['To'] = "dhrumilg699@gmail.com"

msg.set_content("mail demo for otp")

msg.add_alternative("""\
    <html>
    <body>
        <h1> otp : """ + str(otp) + """ </h1>                                       
    </body>
    </html>
    """, subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)
