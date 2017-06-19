# BP Copilot

Code for the Copilot project, winner of the June 2017 BP-Imperial Hackathon Innovation Prize.


We use computer vision to track the sleepiness of a driver in real
time, both with natural light and in darkness using an IR lamp.
When fatigue is detected, an automatic trigger is sent to a Lex Copilot chatbot
that engages with the driver and assists him on the road through simple tasks.


![](ezgif.com-video-to-gif.gif)

We built our own chatbot with [Lex](https://aws.amazon.com/lex/) since [Alexa](https://developer.amazon.com/alexa)
does not allow yet it's programmatic activation.

So far, the following capabilities are available:

 - The image recognition software is able to identify the driver by his name.
 - To read out loud where the nearest BP gas station is, based on your geolocation.
 - To send an automated SMS to one of your pre-defined contacts.
 - To call the emergency services with a pre-recorded message.
 - To play some music for you!

## The Rubber Ducks Team

#### Industrial Design, Business and Marketing strategy
- [Gwen Gage](https://www.linkedin.com/in/gwen-gage-332bba74/)
#### Computer Vision Team
- [Axel Barroso](https://github.com/axelBarroso)
- [Adrian López](https://github.com/alopezgit)
#### Integration and set up
- [Joan Pujol](https://github.com/Jspujol): Google Maps for geolocation
- [Eduardo González](https://github.com/edugp): Twilio, Flask
- [Pablo Pérez](https://github.com/PabStark): AWS Lex and Polly
- [Juan Eiros](https://github.com/jeiros): AWS Lex and Polly
