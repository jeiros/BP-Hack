from twilio.rest import Client
from contact_list import contact_list


def text_friend(user_name='John'):
    if user_name in contact_list:
        number = contact_list[user_name]
    else:
        number = contact_list['John']

    # Find these values at https://twilio.com/user/account
    account_sid = "AC636666ef83e1ec06714c5114b07aaddf"
    auth_token = "565fc1ea9721d1bdae1822ae6d1dae69"
    client = Client(account_sid, auth_token)

    my_twilio_number = "+441423740800"
    text = "Your friend is driving and tired. Please, try contacting him."
    try:
        message = client.api.account.messages.create(to=number,
                                                     from_=my_twilio_number,
                                                     body=text)
    except:
        pass