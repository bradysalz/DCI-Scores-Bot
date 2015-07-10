import praw

from config import username, password


class RedditBot():
    """Bot that browses reddit"""

    base_url = 'http://reddit.com/r/'
    def __init__(self, subreddit='dcicsstest'):
        # <platform>:<app ID>:<version string> (by /u/<reddit username>)
        self.__agent__ = 'python:dci-scores-tracker:1.0 (by /u/dynerthebard)'
        self.__conn__ = praw.Reddit(user_agent=self.__agent__)
        self.__conn__.login(username, password, disable_warning=True)
        self.subreddit = subreddit
        # print self.__conn__

    def random_print(self):
        print 'hi'

    def get_redditor(self, username):
        return self.__conn__.get_redditor(username)

    def post_thread(self, title, body):
        self.__conn__.submit(self.subreddit, title, body)

    def get_footer(self):
        return (
            "*I'm a bot! Check me out on [GitHub](https://github.com/bradysalz/DCI-Scores-Bot)!"
            " Please PM me with any additional feedback.*"
            "\n\n"
            "*Hope you enjoy!*")

    def parse_show_to_table(self, show):
        text = '###' + show['name'] + '\n\n'
        text += '##' + show['date'] + '\n##Judged by ' + show['judge']
        text += self.get_spacer()

        # print show['categories']
        temp_row = [r for r in show['categories'] if r != u'\n\n']
        temp_row.insert(0, '|'+show['class'])
        temp_row.append('Total')
        text += self.append_row(temp_row)

        col_cnt = len(temp_row)
        temp_row = ''
        for i in xrange(col_cnt):
            temp_row += '--|'
        text += temp_row + '\n'

        temp_row = [j for j in show['judges'] if j != '\n\n']
        temp_row.insert(0, '|Judges')
        text += self.append_row(temp_row)

        for i in xrange(len(show['corps'])):
            temp_row = show['corps'][i] + '|'
            temp_row += '|'.join(show['subcaptions'][i])
            temp_row += '|' +  '**'+show['totals'][i]+'**'
            temp_row += '\n'
            text += temp_row

        text += '\n\nFull recap available [here]({0})\n\n'.format(show['url'])
        text += '\n'

        with open('redditoutput.text', 'wb') as f:
            f.write(text)

        return text

    def append_row(self, row):
        output = ''
        for r in row:
            if r:
                output += r + '|'
        output += '\n'
        return output

    def get_spacer(self):
        return '''\n\n

^^^^^^^^^^^^^^^^yes-you-need-this-text-here

-----
&nbsp;\n\n'''
