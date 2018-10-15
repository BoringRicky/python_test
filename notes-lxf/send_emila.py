
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr,formataddr
import smtplib


def _format_addr(address):
    name,addr = parseaddr(address)
    return formataddr((Header(name,'utf-8').encode(),addr))

#发送邮件的邮箱
from_address = 'litengit@163.com'
#发送邮件的密码
password = '19901128liteng'

to_address = '小腾腾<litengit@163.com>'

smtp_server = 'smtp.163.com'
email_content = 'Hello,send by Python ...'

msg = MIMEText(email_content,'plain','utf-8')
# 标题
msg['Subject'] = '自己发送'
# 来自于
msg['From'] = from_address
# 发送给
msg['To'] = _format_addr(to_address)


server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_address,password)
server.sendmail(from_address,[to_address],msg.as_string())
server.quit()



