from flask import Flask, render_template, request, redirect
import twilio.twiml 
from twilio.rest import TwilioRestClient
import random
import pywapi
# Your Account Sid and Auth Token from twilio.com/user/account

app = Flask(__name__)
callers = {
  "+447592489123": "Ramona",
   "447592489123": "Boots",
   "07592489123": "Virgil",
}

weather_com_London = pywapi.get_weather_from_weather_com('UKXX0085')
weather_com_Edi = pywapi.get_weather_from_weather_com('UKXX0052')
weather_com_Aberdeen = pywapi.get_weather_from_weather_com('UKXX0001')
weather_com_Manchester = pywapi.get_weather_from_weather_com('UKXX0092')
weather_com_Liverpool = pywapi.get_weather_from_weather_com('UKXX0083')

diets=["Eat an apple","Don't eat anything","Throw away all the chocolate", "Leave the house"]

quotes=["Rabbits are funny-Eintein", "Rain is wet-Eintein", "Sun is not wet-Einstein", "Tornados can destroy your house- Some smart guy", "There is really no such thing as bad weather, only different kinds of good weather.","Wherever you go, no matter what the weather, always bring your own sunshine","Weather forecast for tonight: dark.","I'm leaving because the weather is too good. I hate London when it's not raining.-Groucho Marx","In the Spring, I have counted 136 different kinds of weather inside of 24 hours. -Mark Twain","Who cares about the clouds when we're together? Just sing a song and bring the sunny weather.-Dale Evans"]

l="Weather.com says: It is " + weather_com_London['current_conditions']['text'].lower() + " and " + weather_com_London['current_conditions']['temperature'] + "C now in London."

e= "Weather.com says: It is " + weather_com_Edi['current_conditions']['text'].lower() + " and " + weather_com_Edi['current_conditions']['temperature'] + "C now in Ediburgh."


a="Weather.com says: It is " + weather_com_Aberdeen['current_conditions']['text'].lower() + " and " + weather_com_Aberdeen['current_conditions']['temperature'] + "C now in Aberdeen."

m="Weather.com says: It is " + weather_com_Manchester['current_conditions']['text'].lower() + " and " + weather_com_Manchester['current_conditions']['temperature'] + "C now in Manchester."

li="Weather.com says: It is " + weather_com_Liverpool['current_conditions']['text'].lower() + " and " + weather_com_Liverpool['current_conditions']['temperature'] + "C now in Liverpool."


def send():
	account_sid = "ACc6bf0f1ef7aaf5aaaaea83919d793519"
	auth_token = "77299b8451acd0ff304a6537e52af71a"
	client = TwilioRestClient(account_sid, auth_token)
	message = client.messages.create(body="It's time to eat healthy <3",
	to="447592489123", # Replace with your phone number
	from_="441937302020") # Replace with your Twilio number

@app.route("/phone", methods=['GET', 'POST'])
def hello_monkey():
	"""Respond and greet the caller by name."""
	from_number = request.values.get('From', None)
        body_mes = request.values.get('Body', None)
        message="Wrong input"
	if body_mes=="Weather London":
	   message=l
        if body_mes=="Weather Edi":
	   message=e
        if body_mes=="Weather Glasgow":
	   message=g
        if body_mes=="Weather Aberdeen":
           message=a
        if body_mes=="Weather Liverpool":
           message=li
        if body_mes=="Weather Manchester":
           message=m
        if body_mes=="Diet":
           message=random.choice(diets)
	if body_mes=="Quote":
           message=random.choice(quotes)
	resp = twilio.twiml.Response()
	resp.message(message)

	return str(resp)

	

@app.route('/')
def home():
  return render_template('home.html')
  
@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/TextLondon')
def TextLondon():
  return render_template('TextLondon.html')

@app.route('/TextManchester')
def TextManchester():
  return render_template('TextManchester.html')

@app.route('/TextLiverpool')
def TextLiverpool():
  return render_template('TextLiverpool.html')

@app.route('/TextEdinburgh')
def TextEdinburgh():
  return render_template('TextEdinburgh.html')

@app.route('/TextAberdeen')
def TextAberdeen():
  return render_template('TextAberdeen.html')

@app.route('/TextGlasgow')
def TextGlasgow():
  return render_template('TextGlasgow.html')

@app.route('/sth')
def sth():
    hello_monkey()
    return "If you sent the right message you should have received an answer"

@app.route('/sth2')
def sth2():
    send()
    return "The memo was sent"
  
  
if __name__ == '__main__':
  app.run(debug=True)
