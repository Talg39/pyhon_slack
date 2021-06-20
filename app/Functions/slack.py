import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
import sys
import datetime

logging.basicConfig(level=logging.DEBUG)


class UrlSlackBot:
    def __init__(self, token, channel):
        self.token = token
        self.channel = channel
        self.client = WebClient(token=token)

    def send_message(self, message):
        try:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            response = self.client.chat_postMessage(
                channel=self.channel,
                text=f'{message} send by user: {get_username()} at {now}'
            )
            logging.info(response)
        except SlackApiError as e:
            logging.error(f'failed to send message: {e.response["error"]}')


def get_username():
    if 'win' in sys.platform:
        return os.getlogin()
    return os.environ.get('USER')
