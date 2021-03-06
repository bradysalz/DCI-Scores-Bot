import re

import praw

from config import username, password


class RedditBot():
    """Bot that browses reddit"""

    def __init__(self, subreddit='dcicsstest'):
        # <platform>:<app ID>:<version string> (by /u/<reddit username>)
        self.__agent__ = 'python:dci-scores-tracker:1.0 (by /u/dynerthebard)'
        self.__conn__ = praw.Reddit(user_agent=self.__agent__)
        self.__conn__.login(username, password, disable_warning=True)
        self.subreddit = subreddit
        self.replacements = {
            'General Effect ': 'GE',
            'Visual Proficiency': 'VP',
            'Visual - Analysis': 'VA',
            'Music - Brass': 'MB',
            'Music - Analysis': 'MA',
            'Music - Percussion': 'MP',
            'Color Guard': 'CG',
            'Penalties': 'P'
        }
        # print self.__conn__

    def post_thread(self, title, body):
        self.__conn__.submit(self.subreddit, title, body)

    def get_footer(self):
        return (
            "*I'm a bot! Check me out on [GitHub](https://github.com/bradysalz/DCI-Scores-Bot)!"
            " Please PM me with any additional feedback.*"
            "\n\n"
            "*Hope you enjoy!*")


    def parse_show_to_post_2016(self, show):
        # redone for new show format in 2016
        body_text = ''

        # header row
        body_text += '\n CORPS |' + ' | '.join(show['categories']) + '\n'

        # alignment
        body_text += ':--|' + '|'.join([':--' for _ in show['categories']]) + '\n'

        # row for each corps
        for cnt, corps in enumerate(show['corps']):
            captions = show['captions']
            row = corps + ' | '
            row += '|'.join(captions[4*cnt : 4*cnt+3])
            row += '|' + show['penalties'][cnt]
            row += '|' + show['totals'][cnt] + '\n'
            body_text += row

        body_text += '\n\nFull recap available [here]({0})\n\n'.format(show['url'])
        body_text += '\n'

        return body_text



    def parse_show_to_post(self, show):
        ## removed all of this, got too big for reddit table
        # text = ''
        # temp_row = [r for r in show['categories'] if r != u'\n\n']
        # temp_row.insert(0, '|' + show['class'])
        # if 'Total' not in temp_row:
        #     temp_row.append('Total')
        # text += self._shorten_caption_names(self.append_row(temp_row))
        #
        # col_cnt = len(temp_row)
        # temp_row = ''
        # for i in xrange(col_cnt):
        #     temp_row += '--|'
        # text += temp_row + '\n'
        #
        # temp_row = [j for j in show['judges'] if j != '\n\n']
        # temp_row.insert(0, '|Judges')
        # text += self.append_row(temp_row)

        text = show['class'] + '|Score\n--|--\n'
        for i in xrange(len(show['corps'])):
            temp_row = show['corps'][i] + '|'
            # temp_row += '|'.join(show['subcaptions'][i])
            temp_row += '**' + show['totals'][i] + '**'
            temp_row += '\n'
            text += temp_row

        text += '\n\nFull recap available [here]({0})\n\n'.format(show['url'])
        text += '\n'

        return text

    def get_header(self, show):
        text = '###' + show['name'] + '\n\n'
        text += '##' + show['date'] + '\n##Head Judge: ' + show['judge']
        text += self.get_spacer()
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

    def _shorten_caption_names(self, cap_str):
        # thanks stack overflow for this chunk
        # http://stackoverflow.com/questions/6116978/python-replace-multiple-strings

        rep = dict((re.escape(k), v) for k, v in self.replacements.iteritems())
        pattern = re.compile("|".join(rep.keys()))
        return pattern.sub(lambda m: rep[re.escape(m.group(0))], cap_str)

    def get_legend(self):
        legend =  'GE -> General Effect\n\n'
        legend += 'VP -> Visual Proficiency\n\n'
        legend += 'VA -> Visual Analysis\n\n'
        legend += 'CG -> Color Guard\n\n'
        legend += 'MB -> Music - Brass\n\n'
        legend += 'MA -> Music - Analysis\n\n'
        legend += 'MP -> Music - Percussion\n\n'
        legend += 'P -> Penalties\n\n'

        return legend

