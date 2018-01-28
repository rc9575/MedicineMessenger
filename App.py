from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.rest import Client
import urllib


account_sid = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

client = Client(account_sid, auth_token)
app = Flask(__name__)

@app.route("/")
def get_form():
    return render_template("form.html")

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        info1 = request.form.get('prescription')
        info2 = request.form.get('cellnum')
        result = request.form
        return render_template("result.html", result=result)
list_of_responses = {}
messages_received = {}

@app.route('/sms', methods=['GET','POST'])
def inbound_sms():
    message = urllib.parse.unquote(request.form['Body'])

    if request.form['From'] in messages_received:
        None
    else:
        messages_received[request.form['From']] = False

    if messages_received[request.form['From']] is False:
        if message == "Yes":
            messages_received[request.form['From']] = True
            if request.form['From'] in list_of_responses:
                list_of_responses[request.form['From']] += 1
            else:
                list_of_responses[request.form['From']] = 1

            for i in list_of_responses:
                print(i + " " + str(list_of_responses[i]))
            response = MessagingResponse()
            response.message("Response Recorded")
            return str(response)

        elif(message == 'No'):
            response = MessagingResponse()
            response.message("Response Recorded")
            messages_received[request.form['From']] = True
            for i in list_of_responses:
                print(i + " " + str(list_of_responses[i]))
            return str(response)

        else:
            response = MessagingResponse()
            response.message("Please respond Yes or No")

            for i in list_of_responses:
                print(i + " " + str(list_of_responses[i]))

            return str(response)
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


