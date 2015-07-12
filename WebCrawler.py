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
        pass

    def update_show_list(self):
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

    def parse_recap_table(self, recap_url):
        r = requests.get(recap_url)
        page = bs4.BeautifulSoup(r.content, 'html5lib')

        # get basic show info
        header = page.body.find_all('table')[0]
        show_name = header.tbody.tr.td.next_sibling.next_sibling.contents[1].string
        show_date = header.tbody.tr.td.next_sibling.next_sibling.contents[5].string

        chief_judge = page.body.find_all("div", class_="chiefJudge")[0].contents[0][13:]

        score_table = page.body.find_all('table')[1]
        class_type = score_table.tbody.tr.td.contents[0]

        score_table = score_table.tbody.find_all('tr')[1].td.table.tbody

        caption_offset = self.is_caption(score_table.tr.find_all('td')[1].string)

        # get categories
        categories = score_table.tr
        if caption_offset == 1:
            categories = categories.next_sibling

        category_list = []
        for cat in categories:
            if cat.string != u'\n' and cat.string != u'\xa0':
                category_list.append(cat.string)

        # get judges
        judges = categories.next_sibling
        judge_list = []
        for judge in judges:
            if judge.string != u'\n' and judge.string != u'\xa0':
                judge_list.append(judge.string)

        # get scores
        corps_list = []
        subcaption_list = []
        caption_total_list = []
        penalty_list = []
        total_list = []

        for row in score_table.find_all('tr', recursive=False)[3+caption_offset:]:
            corps_name =  row.td.string
            corps_list.append(corps_name)

            subcaptions = row.find_all('td', class_='subcaptionTotal')
            subcaptions = [sb.table.tr.td.string for sb in subcaptions]
            subcaption_list.append(subcaptions)

            caption_total = row.find_all('td', class_='categoryTotal')
            caption_total = [ct.table.tr.td.string for ct in caption_total]
            caption_total_list.append(caption_total)

            penalty = row.find_all('td', recursive=False)[-2].table.tbody.tr.td.string
            penalty_list.append(penalty)

            total = row.find_all('td', recursive=False)[-1].table.tbody.tr.td.string
            total_list.append(total)

        show = {
            "name": show_name,
            "date": show_date,
            "judge": chief_judge,
            "judges": judge_list,
            "class": class_type,
            "categories": category_list,
            "corps": corps_list,
            "subcaptions": subcaption_list,
            "captions": caption_total_list,
            "penalties": penalty_list,
            "totals": total_list,
            "url": recap_url
        }

        return show

    def is_caption(self, cap):
        bad_headers = [u'General Effect', u'Visual Analysis', u'Visual', u'Music', u'Effect']
        if cap in bad_headers:
            return 1
        return 0