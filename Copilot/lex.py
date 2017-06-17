"""Getting Started Example for Python 2.7+/3.3+"""
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir

lex_session = Session(profile_name="adminuser", region_name="us-east-1")
lex = lex_session.client("lex-runtime")

def trigger():
    response = lex.post_text(
     botName='CopilotBot',
     botAlias='copilotbotpablo',
     userId='TheRubberDucks',
     sessionAttributes={
         'string': 'string'
     },
     inputText='TRIGGER COPILOT'
    )
    print(response)
    #message = response['message']
    #return message

