import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

with open("Mailler.txt", "r", encoding="utf-8") as file:
    for i in file:
        i = i[:-1]
        list_mail = i.split(",")
        name = list_mail[0]
        mail = list_mail[1]

        message = MIMEMultipart()
        # Mail which is you want to send from
        message["From"] = "sendermail@gmail.com"
        # Mail which is you want to send to
        message["To"] = mail
        # Mail subject
        message["Subject"] = "Smpt automatic mail sender"
        # Mail texts
        text = """
            Hello Mr/Ms{}
        Smpt automatic mail sender.
        your texts are here

        """.format(name)

        body_mail = MIMEText(text)
        message.attach(body_mail)

        try:
            # Gmail lets us to use 587 port to send mails
            mail = smtplib.SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            # Enter your mail and pasword here below
            mail.login("sendermail@gmail.com", "************")
            mail.sendmail(message["From"], message["To"], message.as_string())
            print("Mail sent successfully")
            mail.close()
        except:
            sys.stderr.write("an error happened")
            sys.stderr.flush()
