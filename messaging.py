from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC6623607277e4e5c5fd998bcad0071f13'
auth_token = '372758d3985407f5cd50e20ef95baf60'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there!',
                              from_='whatsapp:+919781379838',
                              to='whatsapp:+918194952848'
                          )

print(message.sid)