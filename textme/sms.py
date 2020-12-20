from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+1',
    body='Do you know BTS?',
    to='+1'
)

print(message.sid)
