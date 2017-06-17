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

def getMessage(response):
    if(response['dialogState'] == 'ConfirmIntent'):
        return response['message']
    elif(response['dialogState'] == 'ReadyForFulfillment'):
        return "ReadyForFulfillment"
    elif(response['dialogState'] == 'Failed'):
        return response['message']
    elif(response['dialogState'] == 'ElicitIntent'):
        return response['message']
    else:
        return None


def call_police():
    response = lex.post_text(
        botName='CopilotBot',
        botAlias='Prod',
        userId='TheRubberDucks',
        sessionAttributes={
            'string': 'string'
        },
        inputText='Call the police'
    )
    return getMessage(response)


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


def text_contact(person):
    from contact_list import contact_list
    response = lex.post_text(
        botName='CopilotBot',
        botAlias='Prod',
        userId='TheRubberDucks',
        sessionAttributes={
            'string': 'string'
        },
        inputText='text %s' % person
    )
    contact = response['slots']['CONTACT']
    if contact in contact_list:
        print(contact_list[contact])
    # return response


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

def spoken_no():
    file_w = open('./stereo_file.wav', 'r')
    audio_stream = file_w.read
    response = lex.post_content(
        botName='CopilotBot',
        botAlias='Prod',
        userId='pablopg',
        sessionAttributes={
            'string': 'string'
        },
        accept = 'text/plain; charset=utf-8',
        contentType='audio/L16; rate=16000; channels=1',
        inputStream= 'yes.wav'
    )

    print(response)
    return getMessage(response)