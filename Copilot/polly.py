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
import audio


# Create a client using the credentials and region defined in the [adminuser]
# section of the AWS credentials file (~/.aws/credentials).
session = Session(profile_name="default")
polly = session.client("polly")
id_n = 0

def polly_play(input_str):
    global id_n
    id_n = id_n + 1
    try:
        # Request speech synthesis
        response = polly.synthesize_speech(Text=input_str, OutputFormat="mp3",
                                           VoiceId="Kendra")
    except (BotoCoreError, ClientError) as error:
        # The service returned an error, exit gracefully
        print(error)
        sys.exit(-1)

    # Access the audio stream from the response
    if "AudioStream" in response:
        # Note: Closing the stream is important as the service throttles on the
        # number of parallel connections. Here we are using contextlib.closing to
        # ensure the close method of the stream object will be called automatically
        # at the end of the with statement's scope.
        with closing(response["AudioStream"]) as stream:
            output = os.path.join(gettempdir(), "speech"+str(id_n)+".mp3")

            try:
                # Open a file for writing the output as a binary stream
                with open(output, "wb") as file:
                    file.write(stream.read())
                    file.close()
            except IOError as error:
                # Could not write to file, exit gracefully
                print(error)
                sys.exit(-1)

    else:
        # The response didn't contain audio data, exit gracefully
        print("Could not stream audio")
        sys.exit(-1)

    # Play the audio using python

    audio.play_mp3(output, 1.0)