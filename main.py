"""
Making a score reader bot
Brady Salz
6/22/15
"""
import time

from ListManager import ListManager

while True:
    updater = ListManager()
    updater.update_show_list()
    updater.diff_show_post_lists()

    time.sleep(60*10) # wait 10 minutes in between checks, can be lowered