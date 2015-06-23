import praw

class RedditBot:
    """Bot that browses reddit"""
    def __init__(self):
        # <platform>:<app ID>:<version string> (by /u/<reddit username>)
        self.__agent__ = 'python:dci-scores-tracker:1.0 (by /u/dynerthebard)'
        self.__conn__ = praw.Reddit(user_agent=self.__agent__)
        print self.__conn__

    def printStuff(self):
        print 'hi'

    def getRedditor(self, username):
        return self.__conn__.get_redditor(username)

