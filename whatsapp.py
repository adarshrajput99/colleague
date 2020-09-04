from twilio.rest import Client

account_sid = 'AC6623607277e4e5c5fd998bcad0071f13'
auth_token = '372758d3985407f5cd50e20ef95baf60'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='h',
    to='whatsapp:+918194952848'
)

print(message.sid)