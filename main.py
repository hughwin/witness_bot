import os
import praw
from dotenv import load_dotenv

load_dotenv()


def start():
    reddit = praw.Reddit(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        password=os.getenv("PASSWORD"),
        user_agent=os.getenv("USER_AGENT"),
        username=os.getenv("REDDIT_USERNAME"),
    )
    print(reddit.user.me())


if __name__ == '__main__':
    start()


