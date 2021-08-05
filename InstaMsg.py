from instabot import Bot
import time
import datetime
import instabot
from requests.sessions import session

# Enter Username and Password
user = str(input("Enter Username: "))
password = str(input(("Enter Password: ")))

# Initiate the program
ibot = Bot()

# Login to you account
ibot.login(username = user, password = password)

# Enter the message you wanna send
msg = str(input("Enter the message"))

# Reciever Username
receiver = str(input("To whom you want to send the message: "))

# Infinity loop to send message everyday
while True:
    # Get current time and hour
    time = datetime.datetime.now()
    hour = time.hour
    
    if hour == 7:
        ibot.send_message(msg,[receiver])
        l = l + 1
        time.sleep(86400)
    else:
        pass
