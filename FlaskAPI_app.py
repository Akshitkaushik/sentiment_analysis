from distutils.log import debug
from flask import Flask,request
from googlesearch import search
import requests
from twilio.twiml.messaging_response import MessagingResponse
import os
from twilio.rest import Client
import smtplib
from email.message import EmailMessage


import email, smtplib, ssl

import time
import json

app = Flask(__name__)

@app.route("/", methods=["POST"])

# # chatbot logic
def bot():

	# user input
	user_msg = request.values.get('Body', '').lower()
	a = request.values.get('status', '').lower()
	print(a)
	user_mssg=list(user_msg)
	if len(user_mssg)!=0:

		account_sid = "ACf8ac8e01c12aff52a39b2ae886051e2f"
		auth_token = "604d57948cf9884186c6a31c2bc5db4f"
		client = Client(account_sid, auth_token)

		message = client.messages .create(body="Here's that picture of an owl you requested.",media_url=['https://demo.twilio.com/owl.png'],from_='whatsapp:+14155238886',to='whatsapp:+919990724477')
		print(message.sid)

		mailserver = smtplib.SMTP('outlook.com', 587)
		mailserver.ehlo()
		mailserver.starttls()
		mailserver.login('akshit.kaushik@in2ittech.com', 'Admin@2022')
		mailserver.sendmail('akshit.kaushik@in2ittech.com', 'akshit.kaushik@in2ittech.com', user_msg)
		mailserver.quit()

		print('done')

	# creating object of MessagingResponse
	response = MessagingResponse()

	# User Query
	q = user_msg + "geeksforgeeks.org"

	# list to store urls
	

	# displaying result
	
	msg = response.message('hello')

	

	return str(response)


if __name__ == "__main__":
	app.run(debug=True)







