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

#counter of how many times program has run
x = 0

#counter of how many times word document was written to
y = 0




while True:
    for submission in subreddit.new():
        sub = submission.subreddit
        if sub.over18:
            continue
            #print("NSFW")

        elif sub == "politics":
            continue
            #print("politics")

        elif submission.is_self == True:
            writeData = f"Post by:\n\n{submission.author}\n\n"
            p = document.add_paragraph(writeData)
            p.add_run(f"{submission.title}\n\n").bold = True
            p.add_run(f"{submission.selftext}\nr/{sub}")
            document.add_paragraph("-------------------------------")
            document.save("posts.docx")
            #print("This is a self post")


            y+=1


        elif "reddit.com/r" not in submission.url:
            #print(submission.url)
            postUrl = submission.url
            formattedLink = f"www.reddit.com{submission.permalink}"
            writeData = formattedLink[:-1]
            document.add_paragraph(writeData)
            document.add_paragraph("-------------------------------")
            document.save("posts.docx")

            y+=1

        elif "snap" or "snapchat" in submission.title:
            continue

        x+=1
        print(x)

        if x == 5:
            print(f"Wrote to word document {y} times")
            exit()
