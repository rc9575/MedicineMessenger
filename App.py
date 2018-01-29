from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.rest import Client
from messaging import send_messages
from multiprocessing import Process, Value
import urllib
import schedule
import time

account_sid = "" #input your own
auth_token = ""

client = Client(account_sid, auth_token)
app = Flask(__name__)

@app.route("/")
def get_form():
    return render_template("form.html")

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        info1 = request.form.get('drug')
        info2 = request.form.get('frequency')
        info3 = request.form.get('duration')
        numba = request.form.get('cellnum')
        schedule.every().day.at("2:33").do(send_messages, "ved", info1)
        schedule.run_all()
        result = request.form
        return render_template("result.html", result=result)


#you had to use mothafuckin flask-celery ass shit for this, but in the duration of this hackathon, we were unable to use motherfuckin flask-ass celery shit. Thank you.
# def loop_de_doop():
#     while True:
#         schedule.run_pending()



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
    # loopin_on = Value('b', True)
    # p = Process(target=loop_de_doop(), args=(loopin_on,))
    # p.start()
    app.run(host='0.0.0.0', debug=True)
    #p.join()


