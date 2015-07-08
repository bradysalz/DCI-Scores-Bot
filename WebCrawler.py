import json

import requests
import bs4


class WebCrawler:
    """
    Crawls to dci.org/scores and browses scores
    Saves scores to local txt file
    Should/will update to a database later
    """
    def __init__(self):
        print 'init'

    def update_scores_to_list(self):
        competitions_url = "http://bridge.competitionsuite.com/api/orgscores/GetCompetitionsByOrganization/jsonp"
        DCI_ID = '96b77ec2-333e-41e9-8d7d-806a8cbe116b'
        competition_keys = {'organization':DCI_ID, 'callback':'jQuery'}

        r = requests.get(competitions_url, params=competition_keys)
        json_body = r.content[7:-2]
        scores_dict = json.loads(json_body)

        with open('showlist.csv','wb') as f:
            for comp in scores_dict['competitions']:
                line = ', '.join([comp['name'], comp['competitionDate'], comp['competitionGuid']])
                f.write(line)
                f.write('\n')

    def get_show_recap_url(self, comp_guid):
        comp_url = "http://bridge.competitionsuite.com/api/orgscores/GetCompetition/jsonp"
        keys = {'competition':comp_guid, 'callback':'jQuery'}
        r = requests.get(comp_url, params=keys)
        json_body = r.content[7:-2]
        show = json.loads(json_body)

        recaps = []
        for round in show['rounds']:
            recaps.append(round['recapUrl'])

        return recaps

    def is_show_in_list(self, show_id):
        pass

    def parse_recap_table(self, recap_url):
        r = requests.get(recap_url)
        page = bs4.BeautifulSoup(r.content, 'html5lib')

        chief_judge = page.body.find_all("div", class_="chiefJudge")[0].contents[0][13:]

        score_table = page.body.find_all('table')[1]
        class_type = score_table.tbody.tr.td.contents[0]


        print chief_judge, class_type







