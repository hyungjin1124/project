# send message to user
from twilio.rest import Client
import json

with open("config.json", 'r') as f:
    config = json.load(f)

# send SMS
ACCOUNT_SID = config["DEFAULT"]["ACCOUNT_SID"]
AUTH_TOKEN = config["DEFAULT"]["AUTH_TOKEN"]

class Notification:
    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages \
                .create(
                    body=message,
                    from_='+19108382898',
                    to=config["PRIVATE"]["TO_NUMBER"]
                )

        print(message.status)