import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Luigi Lantin'
email['to'] = 'babypython1@gmail.com'
email['subject'] = 'You got no jams'

email.set_content(html.substitute({'name': 'Namjoon'}), 'html')

# sets host as gmail
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('babypython1@gmail.com', '')
    smtp.send_message(email)
    print('all good boss mane')
