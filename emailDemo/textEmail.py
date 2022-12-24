import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'Training Invitation'
msg['From'] = 'Automation Training Team'
msg['To'] = "vvishwa@gmail.com"
msg.set_content("Test Email from Automation Team")

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("selenium3bymukesh@gmail.com", "Demo@123456")
server.send_message(msg)
server.quit()


