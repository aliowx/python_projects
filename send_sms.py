from email.message import EmailMessage 
from password import passwords
import ssl
import smtplib

email_sender = " alialibakhshi9898@gmail.com "
email_password = "" 


email_resiver = ["@gmail.com" ,"@gmail.com" ]

subject = "hi my name is ali as you know that this is a text of the python programming also"
body="""
So do not worry about Anything i'm here to kill you  
"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_resiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_resiver,em.as_string())
