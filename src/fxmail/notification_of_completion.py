# -*- coding: UTF-8 -*-
import sys, os, re, urllib, urlparse
import smtplib
import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendmail(subject, msg, toaddrs, fromaddrs, smtpaddrs, password):
    # @subject:邮件主题
    # @msg:邮件内容
    # @toaddrs:收信人的邮箱地址
    # @fromaddrs:发信人的邮箱地址
    # @smtpaddr:smtp服务地址，可以在邮箱看，比如163邮箱为smtp.163.com
    # @password:发信人的邮箱密码

    mail_msg = MIMEMultipart()
    if not isinstance(subject, unicode):
        subject = unicode(subject, 'utf-8')

    mail_msg['Subject'] = subject
    mail_msg['From'] = fromaddrs
    mail_msg['To'] = ','.join(toaddrs)
    mail_msg.attach(MIMEText(msg, 'html', 'utf-8'))

    try:
        s = smtplib.SMTP()
        s.connect(smtpaddrs)
        s.login(fromaddrs, password)
        s.sendmail(fromaddrs, toaddrs, mail_msg.as_string())
        s.quit()

    except Exception, e:
        print "Error: unable to send email"
        print traceback.format_exc()

if __name__ == '__main__':
    fromaddrs = ""
    toaddrs = ["", "", ""]
    smtpaddrs = "smtp.sina.com"
    subject = ""
    password = ""
    msg = ""
    sendmail(subject, msg, toaddrs, fromaddrs, smtpaddrs, password)