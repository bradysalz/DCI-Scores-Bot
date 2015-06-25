"""
Making a score reader bot
Brady Salz
6/22/15
"""

import time
import RedditBot
import WebCrawler

# test = RedditBot.RedditBot()
# test.post_thread('ExplainLikeImConnie', 'Test Post Please Ignore', 'I L L\n\nI N I')

test = WebCrawler.WebCrawler()
for att in dir(test.pages):
    if att[0] != '_':
        print att

print test.pages.http_status
print test.pages.url
# print test.resources