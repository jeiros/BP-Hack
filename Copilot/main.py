"""
    Author: pablopg.
    Step-by-step:
        1. Run pip install boto3
        2. Run pip install --upgrade --user awscli (http://docs.aws.amazon.com/cli/latest/userguide/installing.html)
        3. Add awscli to the path (http://docs.aws.amazon.com/cli/latest/userguide/awscli-install-windows.html#awscli-install-windows-path)
        4. Create an user in the AWS CLI.
        5. Configure local AWS cli via the command: aws configure --profile adminuser
        6. Run and listen!
"""

"""Getting Started Example for Python 2.7+/3.3+"""
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir

import polly

# Create a client using the credentials and region defined in the [adminuser]
# section of the AWS credentials file (~/.aws/credentials).
lex_session = Session(profile_name="adminuser")
lex = lex_session.client("lex-runtime")

response = lex.post_text(
    botName='TheRubberBot',
    botAlias='TheRubberBot',
    userId='TheRubberDucks',
    sessionAttributes={
        'string': 'string'
    },
    inputText='My eyes are closing'
)

message = response['message']
polly.polly_play(message)