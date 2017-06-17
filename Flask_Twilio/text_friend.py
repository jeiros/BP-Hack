# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "AC636666ef83e1ec06714c5114b07aaddf"
auth_token = "565fc1ea9721d1bdae1822ae6d1dae69"
client = Client(account_sid, auth_token)

my_twilio_number = "+441423740800"
user_name = 'Juan'
phone_number = "+447731513965"
# phone_number = "+447783018326"
# text = "We think your friend {} is falling asleep in the car. Try contacting him".format(user_name)
text = "We think your friend {} is a pussy".format(user_name)
message = client.api.account.messages.create(to=phone_number,
                                             from_=my_twilio_number,
                                             body=text)
