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
        last_show = [l.rstrip() for l in last_show]

        last_post = post_file.readlines()
        last_post = [l.rstrip() for l in last_post]

        show_cnt = 0

        while last_show[show_cnt] not in last_post:
            curr_show = last_show[show_cnt].split(', ')
            crawler = WebCrawler()
            bot = RedditBot('dcibottest')

            recaps = crawler.get_show_recap_url(curr_show[2])
            shows = [crawler.parse_recap_table(r) for r in recaps]
            bodies = [bot.parse_show_to_table(s) for s in shows]

            single_body = bot.get_header(shows[0])
            single_body += '\n\n'.join(bodies)
            single_body += bot.get_footer()

            with open('redditoutput.text', 'wb') as f:
                f.write(single_body)

            post_title = curr_show[0] + ' Scores'
            print post_title

            bot.post_thread(post_title, single_body)

            with file('postlist.csv', 'rb') as original: orig = original.read()
            with file('postlist.csv', 'wb') as modified: modified.write(', '.join(curr_show) + '\n' + orig)

            print 'added new show'
            print last_show[show_cnt]
            show_cnt += 1

        show_file.close()
        post_file.close()

    def update_show_list(self):
        WebCrawler().update_show_list()