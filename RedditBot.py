import praw

from config import username, password

class RedditBot:
    """Bot that browses reddit"""
    def __init__(self):
        # <platform>:<app ID>:<version string> (by /u/<reddit username>)
        self.__agent__ = 'python:dci-scores-tracker:1.0 (by /u/dynerthebard)'
        self.__conn__ = praw.Reddit(user_agent=self.__agent__)
        # self.__conn__.login(username, password)
        self.__conn__.login(username, password, disable_warning=True)
        print self.__conn__

    def random_print(self):
        print 'hi'

    def get_redditor(self, username):
        return self.__conn__.get_redditor(username)

    def post_thread(self, subreddit, title, body):
        self.__conn__.submit(subreddit, title, body)
