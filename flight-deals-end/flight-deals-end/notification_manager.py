import requests

class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.bot_token = '6389852152:AAHB9xxBi-sxB_2WCK7K-pbAhUUmjYSE9vs'
        self.bot_chatID = '6374414086'

    def send_sms(self, message):
        send_text = ('https://api.telegram.org/bot' + self.bot_token + '/sendMessage?chat_id=' + self.bot_chatID +
                     '&parse_mode=Markdown&text=' + message)

        requests.get(send_text)

