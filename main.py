import praw
import time
import os
from docx import *
import pprint
from common import *
from docx import Document

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("all")

document = Document()
document.save("posts.docx")
x = 0
y = 0
self = False
while True:
    for submission in subreddit.new():

    #for submission in subreddit.controversial("day"):

        sub = submission.subreddit
        if sub.over18:
            print("NSFW")

        elif sub == "politics":
            print("politic")

        elif submission.is_self == True:
            self = True
            print("This is a self post")


        elif "reddit.com/r" not in submission.url:
            #print(submission.url)
            postUrl = submission.url
            #Eventually, you will simply add the post URL to the word doc
            postPermaLink = f"reddit.com{submission.permalink}"

        elif "snap" or "snapchat" in submission.title:
            continue

        if x == 10:
            if self == True:
                writeData = f"Post by:{submission.author}\n{submission.title}\n{submission.selftext}\n{sub}\n\n"
                print(writeData)
                #document.add_paragraph(writeData)
                #document.save("posts.docx")
                #y += 1



            else:
                writeData = f"www.{postPermaLink}"
                print(writeData)

            document.add_paragraph(writeData)
            document.save("posts.docx")
            y += 1

        elif x == 20:
            print(f"Wrote to word document {y} times")
            exit()
