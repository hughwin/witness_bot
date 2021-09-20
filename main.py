import os
import praw
import threading
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    password=os.getenv("PASSWORD"),
    user_agent=os.getenv("USER_AGENT"),
    username=os.getenv("REDDIT_USERNAME"),
)


def start():
    while True:
        check_witnesses_thread = threading.Thread(target=check_witnesses())
        check_witnesses_thread.start()

        check_replies_thread = threading.Thread(target=check_replies())
        check_replies_thread.start()


def check_witnesses():
    witness_words = ["Witness me!", "Witness me"]
    for comment in reddit.subreddit("test").stream.comments():
        count = 0
        comment_body = comment.body.strip()
        if any(witness.lower() in comment_body.lower() for witness in witness_words):
            print("String with \"sample user comment\" found in comment " + comment.id)
            comment.reply("Witness!")
            count += 1
            print("Replied to comment " + comment.id)
        print("Comments replied to: {}".format(count))


def check_replies():
    print("Checking for replies")
    good_bot_words = ["goodbot", "good bot", "goodbot!", "good bot!"]
    local_count = 0
    for comment in reddit.inbox.unread(limit=None):
        comment_body = comment.body.strip()
        if any(goodbot.lower() in comment_body.lower() for goodbot in good_bot_words):
            print("Found someone who appreciates the bot!")
            comment.reply("I have witnessed {} witnesses.".format(1))
            comment.mark_read()
        print("Comments replied to: {}".format(local_count))


if __name__ == '__main__':
    start()
