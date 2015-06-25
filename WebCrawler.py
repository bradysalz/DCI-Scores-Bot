import ghost

class WebCrawler:
    """
    Crawls to dci.org/scores and browses scores
    Saves scores to local database
    """
    def __init__(self):
        myGhost = ghost.Ghost(wait_timeout=5)
        url = 'http://www.bradysalz.com/'
        self.pages, self.resources = myGhost.open(url)

