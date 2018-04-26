#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/16 10:03
# @Author  : huanghe
# @Site    : 
# @File    : mail.py
# @Software: PyCharm
import smtplib
from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr,formataddr



class Email:
    def __init__(self,server,sender,password,receiver,subject,title=None,message=None,path=None):
        self.server = server
        self.sender = sender
        self.password = password
        self.receiver = receiver
        self.subject = subject
        self.msg =  MIMEMultipart()
        #self.msg = MIMEText(msg,'plain','utf-8')

    def _format_addr(self,s):
        name,addr = parseaddr(s)
        return formataddr((Header(name,'utf-8').encode(),addr))

    def send(self):
        server = smtplib.SMTP(self.server,25)
        server.set_debuglevel(1)
        server.login(self.sender,self.password)
        server.sendmail(self.sender,[self.receiver],self.msg.as_string())
        server.quit()

    def add_fujian(self,filepath):
        with open(filepath,'rb')as f:
            mime = MIMEBase('image','png',filename='test.png')
            mime.add_header('Content-Disposition', 'attachment',filename='test.png')
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            mime.set_payload(f.read())
            encoders.encode_base64(mime)
            self.msg.attach(mime)

    def set_content(self,msg):
        self.msg['From'] = self._format_addr('发件人<{}>'.format(self.sender))
        self.msg['To'] = self._format_addr('收件人<{}>'.format(self.receiver))
        self.msg['Subject'] = Header(self.subject, 'utf-8').encode()
        self.msg.attach(MIMEText(msg,'plain','utf-8'))


if __name__ == '__main__':
    msg = 'helllo'
    email = Email(server='mail.xor-media.tv',sender='he.huang@xor-media.tv',password='2953653ABCDE'
                  ,receiver='943298665@qq.com',subject='主题')
    email.set_content(msg)
    email.add_fujian('test.png')
    #name,addr = parseaddr('Python爱好者<he.huang@xor-media.tv>')
    #print(formataddr((Header(name,'utf-8').encode(),addr)))
    email.send()