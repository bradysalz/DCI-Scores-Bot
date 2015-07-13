from datetime import datetime
import time

from WebCrawler import WebCrawler
from RedditBot import RedditBot


class ListManager:
    """
    Manages when to make a post
    compares the postlist with the showlist
    """

    def __init__(self):
        pass

    def diff_show_post_lists(self):
        show_file = open('showlist.csv', 'rb')
        post_file = open('postlist.csv', 'rb')

        last_show = show_file.readlines()
        show_list = [l.rstrip() for l in last_show]

        last_post = post_file.readlines()
        post_list = [l.rstrip() for l in last_post]

        for show in show_list:
            if show not in post_list:
                curr_show = show.split(', ')
                crawler = WebCrawler()
                bot = RedditBot('drumcorps')

                recaps = crawler.get_show_recap_url(curr_show[2])
                shows = [crawler.parse_recap_table(r) for r in recaps]
                bodies = [bot.parse_show_to_post(s) for s in shows]

                single_body = bot.get_header(shows[0])
                single_body += '\n\n'.join(bodies)
                single_body += bot.get_legend()
                single_body += bot.get_footer()

                with open('redditoutput.text', 'wb') as f:
                    f.write(single_body)

                post_title = curr_show[0] + ' Scores'

                bot.post_thread(post_title, single_body)

                with open('logging.txt', 'ab') as log:
                    print 'new show' 
                    log.write('added new show on {0}\n'.format(datetime.now()))
                    log.write(show + '\n')

                time.sleep(5*60) # reddit post timeout?

        with open('postlist.csv', 'wb') as p:
            p.write('\n'.join(show_list))

    def update_show_list(self):
        WebCrawler().update_show_list()
