"""Getting Started Example for Python 2.7+/3.3+"""
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir
import json

lex_session = Session(profile_name="adminuser", region_name="us-east-1")
lex = lex_session.client("lex-runtime")

def getMessage(response):
    if(response['dialogState'] == 'ConfirmIntent'):
        return response['message']
    elif(response['dialogState'] == 'ReadyForFulfillment'):
        return "ReadyForFulfillment"
    elif(response['dialogState'] == 'Failed'):
        return response['message']
    else:
        return None

def call_police():
    pass

def eyes_closed():
    response = lex.post_text(
     botName='CopilotBot',
     botAlias='Prod',
     userId='TheRubberDucks',
     sessionAttributes={
         'string': 'string'
     },
     inputText='TRIGGER COPILOT'
    )
    return getMessage(response)

def find_nearest_gas_station():
    pass

def play_music():
    pass

def reset():
    pass

def stop():
    response = lex.post_text(
        botName='CopilotBot',
        botAlias='Prod',
        userId='TheRubberDucks',
        sessionAttributes={
            'string': 'string'
        },
        inputText='Stop'
    )

def text_contact():
    pass


def yes():
    response = lex.post_text(
     botName='CopilotBot',
     botAlias='Prod',
     userId='TheRubberDucks',
     sessionAttributes={
         'string': 'string'
     },
     inputText='Yes'
    )
    return getMessage(response)

def no():
    response = lex.post_text(
     botName='CopilotBot',
     botAlias='Prod',
     userId='TheRubberDucks',
     sessionAttributes={
         'string': 'string'
     },
     inputText='No'
    )
    return getMessage(response)