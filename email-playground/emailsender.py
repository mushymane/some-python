import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Luigi Lantin'
email['to'] = 'babypython1@gmail.com'
email['subject'] = 'You got no jams'

email.set_content('Jimin has funk and soul')

# sets host as gmail
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('babypython1@gmail.com', 'hahahehehoho')
    smtp.send_message(email)
    print('all good boss mane')
