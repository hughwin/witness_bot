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
    witness_words = ["Witness me!", "Witness me"]

    for comment in reddit.subreddit("test").stream.comments():
        count = 0
        cbody = comment.body.strip()
        if any(witness.lower() in cbody.lower() for witness in witness_words):
            print("String with \"sample user comment\" found in comment " + comment.id)
            comment.reply("Witness!")
            count += 1
            print("Replied to comment " + comment.id)
        print("Comments replied to: {}".format(count))


if __name__ == '__main__':
    start()


