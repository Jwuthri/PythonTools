# -*- coding: utf-8 -*-
"""
Created on July 2017

@author: JulienWuthrich
"""
import email
import smtplib


def send_mail(sender, receiver, subject, message, attach_file=None):
    msg = email.mime.multipart.MIMEMultipart()
    msg["From"] = str(object=sender)
    msg["To"] = str(object=receiver)
    msg["Subject"] = str(object=subject)
    msg.attach(email.mime.text.MIMEText(message))
    mailserver = smtplib.SMTP("Julien.Wut@gmail.com", 25)
    if attach_file:
        part = email.mime.base.MIMEBase('application', "octet-stream")
        part.set_payload(open(attach_file, "rb").read())
        email.encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachmement')
        msg.attach(part)

    mailserver.sendmail(sender, receiver, msg.as_string())
    mailserver.quit()
