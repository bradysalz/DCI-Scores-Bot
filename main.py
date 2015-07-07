"""
Making a score reader bot
Brady Salz
6/22/15
"""

import time
import RedditBot
from WebCrawler import WebCrawler

test = WebCrawler()
test.update_scores_to_list()

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




