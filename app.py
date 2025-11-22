from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=["POST"])
def sms_reply():
    resp = MessagingResponse()
    resp.message("Hello! Your message has been received successfully.")
    return str(resp)

