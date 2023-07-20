from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai

app = Flask(__name__)
openai.api_key = process.env.OPENAI_KEY


@app.route("/sms", methods=['POST'])
def sms_reply():
    # Fetch the message
    msg = request.form.get('Body')

    # Pass the msg to GPT-4 model
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=msg,
        temperature=0.5,
        max_tokens=100
    )

    # Prepare the response
    resp = MessagingResponse()
    resp.message(response.choices[0].text.strip())

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
