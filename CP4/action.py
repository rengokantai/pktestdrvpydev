__author__ = 'Hernan Y.Ke'
import smtplib
from email.mime.text import MIMEText


class PrintAction:
    def execute(self, content):
        print(content)
