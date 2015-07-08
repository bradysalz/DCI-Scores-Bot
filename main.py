"""
Making a score reader bot
Brady Salz
6/22/15
"""

from WebCrawler import WebCrawler
from RedditBot import RedditBot

test = WebCrawler()
myshow = test.parse_recap_table('http://recaps.competitionsuite.com/42cdb67a-71d3-4b42-b5ca-803ea3c10404.htm')

bot = RedditBot()
bot.parse_show_to_table(myshow)



# test = RedditBot.RedditBot()
# test.post_thread('ExplainLikeImConnie', 'Test Post Please Ignore', 'I L L\n\nI N I')
#
# test = WebCrawler.WebCrawler()
# for att in dir(test.pages):
#     if att[0] != '_':
#         print att
#
# print test.pages.http_status
# print test.pages.url
# print test.resources
# http://bridge.competitionsuite.com/api/orgscores/GetCompetitionsByOrganization/jsonp?organization=http://bridge.competitionsuite.com/api/orgscores/GetCompetitionsByOrganization/jsonp?organization=96b77ec2-333e-41e9-8d7d-806a8cbe116b&callback=jQuery&callback=jQuery
