"""
Making a DCI score reader and reddit poster bot
Brady Salz
6/22/15
"""

import datetime

from ListManager import ListManager



updater = ListManager()
updater.update_show_list()
updater.diff_show_post_lists()

with open('logging.txt', 'a') as f:
    f.write("cron'd at {0}\n".format(datetime.datetime.now()))

