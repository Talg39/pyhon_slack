from Functions import f
from Functions.slack import UrlSlackBot
import os
from pathlib import Path
from dotenv import load_dotenv

if __name__ == "__main__":
    fp = os.path.abspath(__file__)
    env_path = Path(fp).parent.parent / '.env'
    load_dotenv(dotenv_path=env_path)

    slack_token = os.environ["SLACK_API_TOKEN"]
    channel = os.environ["CHANNEL"]
    sc = UrlSlackBot(slack_token, channel)
    # Initialize variables - read input from user
    print("Please enter url with the syntax like 'https://mobideo.com'")
    url = input()
    print('Received url:', url)
    if f.is_valid(url):
        info = f.get_url(url)
        status = (f.decipher_status(info.status_code))
        if status == "OK":
            print("Status code is 200. continue...")
            sc.send_message(f'URL: {url}, status code: {info.status_code}')
        else:
            print("===== Status code is not 200 (", status,"). please provide a url that is up and working, example: "
                  "https://mobideo.com =====")
            sc.send_message(f'URL: {url}, status code: {info.status_code}')
    else:
        print("===== dns is not valid, Please use the syntax as 'https://mobideo.com' =====")
        sc.send_message(f'dns is not valid for URL: {url} please use the syntax as \'https://mobideo.com\'')
