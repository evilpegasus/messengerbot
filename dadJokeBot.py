from fbchat import *

class DadJokeBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        message = message_object.text
        print(message)
    
    """
    returns index of 
    """
    def indexOfJoke(self, message):
        text = message.lower()
        if "im" in text.split() or "i'm" in text.split():
            return True
        elif "i" in text.split():
            
            


# Log the user in
# get email and password from login.txt
f = open("login.txt", "r")
email = f.readline()
consumer_key = email.rstrip('\n')
password = f.readline()
consumer_secret = password.rstrip('\n')
client = DadJokeBot(email, password)

search = input("Name of dad joke target: ")
user = client.searchForUsers(search)[0]
print("user ID: {}".format(user.uid))
print("user's name: {}".format(user.name))
print("user's photo: {}".format(user.photo))
print("Is user client's friend: {}".format(user.is_friend))

client.listen()



# Send a message to yourself
# client.send(Message(text="Testing 1234567890"),thread_id=client.uid, thread_type=ThreadType.USER)

# Log the user out
# client.logout()