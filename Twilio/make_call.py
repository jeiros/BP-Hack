from twilio.rest import Client

# Get these credentials from http://twilio.com/user/account
account_sid = "AC636666ef83e1ec06714c5114b07aaddf"
auth_token = "565fc1ea9721d1bdae1822ae6d1dae69"
client = Client(account_sid, auth_token)

# Make the call
name_to_number = {'edu' : '+447731513965'}
call = client.api.account.calls\
      .create(to=name_to_number['edu'],  # Any phone number
              from_="+441423740800", # Must be a valid Twilio number
            url='https://c38a7761.ngrok.io')
print(call.sid)