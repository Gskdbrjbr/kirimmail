import smtplib

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

fromaddr = "mailpengirim"

toaddr = "mailpenerima"

msg = MIMEMultipart()

msg['From'] = fromaddr

msg['To'] = toaddr

msg['Subject'] = "JUDUL PESAN"

body = "ISI PESAN"

msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login(fromaddr, "codemailpenerima")

text = msg.as_string()

server.sendmail(fromaddr, toaddr, text)

server.quit()


