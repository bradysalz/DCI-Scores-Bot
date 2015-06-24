"""
Making a score reader bot
Brady Salz
6/22/15
"""

import praw
import bs4
import time
import os

# silly windows problems
try:
    from config import *
    import RedditBot

except ImportError: 
    os.chdir(r'C:\Users\Brady\Documents\GitHub\DCI-Scores-Bot')
    from config import *
    import RedditBot

test = RedditBot.RedditBot()
print dir(test)
x = test.getRedditor('dynerthebard')
lst = x.get_comments()

for i in lst:
    print i