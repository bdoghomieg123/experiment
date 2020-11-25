import praw
import time
import os
from docx import *
from common import *


reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("politics")

if not os.path.isfile("posts.docx"):
    document = Document()
    document.save("posts.docx")
    print("Created Docx file within working directory")
    time.sleep(1)
    clear()

elif os.path.isfile("posts.docx"):
    print("File exists. Continuing")
    time.sleep(1)
    clear()


while True:
    for submission in subreddit.controversial():
        sub = submission.subreddit
        if sub.over18:
            print("Subreddit is NSFW")
        elif sub == "politics":
            print("Subreddit is Politics")


        else:
            print(submission.title)"""
