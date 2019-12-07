from fbchat import log, Client
from fbchat.models import *

import time
import stocks
import datetime


#get email and password from login.txt
f = open("login.txt", "r")
email = f.readline()
consumer_key = email.rstrip('\n')
password = f.readline()
consumer_secret = password.rstrip('\n')
#login
client = Client(email, password)
#Check if logged in
if not client.isLoggedIn():
    print("Logging in again...")
    client.login(email, password)
print("Own id: {}".format(client.uid))


#send an update about a stock to user
def send_stock(ticker):
    if stocks.stock_info(ticker)[2] > 0:
        change = "up"
    elif stocks.stock_info(ticker)[2] < 0:
        change = "down"
    else:
        change = "unchanged"
    message = ticker + " stock price is " + change + " $" + str(round(abs(stocks.stock_info(ticker)[2]), 2)) + " today from $" + str(round(stocks.stock_info(ticker)[0], 2)) + " to $" + str(round(stocks.stock_info(ticker)[1], 2)) + "\n\n" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "\nAutomatic update from https://github.com/evilpegasus/twitterbot"
    print(message)
    client.send(Message(text=message), thread_id=user.uid, thread_type=ThreadType.USER)

#search for user objects using a name
users = client.searchForUsers('Jeff')
user = users[0]
print("User's ID: {}".format(user.uid))
print("User's name: {}".format(user.name))
print("User's profile picture URL: {}".format(user.photo))
print("User's main URL: {}".format(user.url))


#This is broken
"""
class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        # If you're not the author, echo
        if author_id != self.uid:
            self.send(message_object, thread_id=thread_id, thread_type=thread_type)

client.listen()
"""
input("Press ENTER to send message")
send_stock("TSLA")




client.logout()
