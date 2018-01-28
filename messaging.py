from twilio.rest import Client
import schedule
import time
from flask import Flask



account_sid = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx"
auth_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx"

client = Client(account_sid, auth_token)

client_name = "Ved"
string1 = "xanax"
string2 = "two times a day" #how many times a day
string3 = "two weeks"

def convert_to_int(number):
    return {
        'daily': 1,
        'twice': 2,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'day': 1,
        'week': 7,
        'weeks': 7,
        'month': 30,
        'months': 30,
    }.get(number)


def numbers_per_day():
    return convert_to_int(string2.partition(' ')[0])


def add_time(first,hours):
    newhour = first + hours

    return newhour

def times_per_day(freq):
    hours = (int)(18 / freq)
    # temp = 14 / freq
    # mins = int((temp-int(temp))* 60)

    times_to_return = [6]
    for i in range(freq-1):
        times_to_return.append(add_time(times_to_return[i],hours))
    if(times_to_return[len(times_to_return)-1] < 8):
        times_to_return[len(times_to_return) - 1] = 8

    return times_to_return



#This converts list of ints into a list of times to be used by schedule
def convert(list_of_times_in_int):
    for i in range(len(list_of_times_in_int)):
        list_of_times_in_int[i] = str(list_of_times_in_int[i]) + ":00"

    return list_of_times_in_int




    # list = string3.split()
    # first = list[0]
    # second = list[1]

for message in client.messages.list():
    if message.direction == 'inbound':
        print(message.body)

# for i in range(convert_to_int(first)):
#     for q in range(convert_to_int(second)):
#

def send_messages():
    message = client.messages.create(
        to="+16233301676",
        from_="+18016152108",
        body="Reminder for " + client_name + ": " + "take " +string1 + " now.")


# timeList = convert(times_per_day(3))
# for i in range(numbers_per_day()):
#     schedule.every().day.at("18:39").do(send_messages)
#

#while True:
 #   schedule.run_pending()
#print(message.sid)
