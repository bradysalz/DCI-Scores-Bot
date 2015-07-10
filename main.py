"""
Making a score reader bot
Brady Salz
6/22/15
"""
#
# from WebCrawler import WebCrawler
# from RedditBot import RedditBot
from ListManager import ListManager
# test = WebCrawler()
#
# my_show = test.parse_recap_table('http://recaps.competitionsuite.com/42cdb67a-71d3-4b42-b5ca-803ea3c10404.htm')
#
# bot = RedditBot()
# bot.parse_show_to_table(my_show)

# test = RedditBot.RedditBot()
# test.post_thread('ExplainLikeImConnie', 'Test Post Please Ignore', 'I L L\n\nI N I')

test = ListManager()
test.update_show_list()
test.diff_show_post_lists()