"""
Making a score reader bot
Brady Salz
6/22/15
"""

from ListManager import ListManager


updater = ListManager()
updater.update_show_list()
updater.diff_show_post_lists()

