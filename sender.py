#built-in libraries used throughout the program
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#initializing the server
host = 'smtp.gmail.com' # here we are using gmail
port = 465

#defined sender mail and targets
# for this you have to change the settings of the email address from google mail to allow 3rd party app to send mails.
username = 'example'
password = '123456'
sender = 'example@gmail.com'
targets = ['test@gmail.com']

#defined msg (temporary)
msg = MIMEMultipart()
msg['Subject'] = 'first mail'
msg['From'] = sender
msg['To'] = ', '.join(targets)

txt = MIMEText('Hey there users')
msg.attach(txt)

#login account and sending email
server = smtplib.SMTP_SSL(host, port)
server.login(username, password)
server.sendmail(sender, targets, msg.as_string())
server.quit()
