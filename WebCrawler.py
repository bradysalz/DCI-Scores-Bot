import ghost

class WebCrawler:
    """
    Crawls to dci.org/scores and browses scores
    Saves scores to local database
    """
    def __init__(self):
        ghost = ghost.Ghost()
        self.pages, self.resources = ghost.open('http://bradysalz.com')
