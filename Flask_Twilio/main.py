# This code is currently up in a remote server (pablopg.dte.us.es).
#
from flask import Flask, request, redirect
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

# Try adding your own number to this list!
callers = {
    "+34651803161": "Pablo Stark",
    "+14158675310": "Boots",
    "+14158675311": "Virgil",
}


@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Say a caller's name, and play an MP3 for them."""
    from_number = request.values.get('From', None)
    if from_number in callers:
        caller = callers[from_number]
    else:
        caller = "Monkey"

    resp = VoiceResponse()
    # Greet the caller by name
    resp.say("Hello " + caller)
    # Play an MP3
    resp.play("http://demo.twilio.com/hellomonkey/monkey.mp3")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
