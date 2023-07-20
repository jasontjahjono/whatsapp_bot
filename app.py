from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai
import os

from boto.s3.connection import S3Connection
openai_key = S3Connection(os.environ['OPENAI_KEY'])

app = Flask(__name__)
openai.api_key = openai_key


# @app.route("/sms", methods=['POST'])
# def sms_reply():
#     # Fetch the message
#     msg = request.form.get('Body')

#     # Pass the msg to GPT-4 model
#     response = openai.Completion.create(
#         engine="gpt-3.5-turbo",
#         prompt=msg,
#         temperature=0.5,
#         max_tokens=100
#     )

#     # Prepare the response
#     resp = MessagingResponse()
#     resp.message(response.choices[0].text.strip())

#     return str(resp)
@app.route("/sms", methods=['POST'])
def sms_reply():
    # Prepare the response
    resp = MessagingResponse()
    resp.message("Hello, WhatsApp!")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
