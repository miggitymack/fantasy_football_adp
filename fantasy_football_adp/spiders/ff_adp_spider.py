from scrapy import Spider, Request
from fantasy_football_adp.items import FantasyFootballAdpItem
import json


class FantasyFootballAdpSpider(Spider):
    name = "ff_adp_spider"
    allowed_urls = ['https://www.pro-football-reference.com']
    start_urls = ['https://www.pro-football-reference.com/years/2019/fantasy.htm']

    def parse(self, response):
        rows = response.xpath('//table/tbody/tr')

        for row in rows:
            player = row.xpath('./td[@data-stat="player"]/a/text()').extract_first()
            pos = row.xpath('./td[@data-stat="fantasy_pos"]/text()').extract_first()
            age = row.xpath('./td[@data-stat="age"]/text()').extract_first()
            g = row.xpath('./td[@data-stat="g"]/text()').extract_first()
            gs = row.xpath('./td[@data-stat="gs"]/text()').extract_first()
            pass_cmp = row.xpath('./td[@data-stat="pass_cmp"]/text()').extract_first()
            pass_att = row.xpath('./td[@data-stat="pass_att"]/text()').extract_first()
            pass_yds = row.xpath('./td[@data-stat="pass_yds"]/text()').extract_first()
            pass_td = row.xpath('./td[@data-stat="pass_td"]/text()').extract_first()
            pass_int = row.xpath('./td[@data-stat="pass_int"]/text()').extract_first()
            rush_att = row.xpath('./td[@data-stat="rush_att"]/text()').extract_first()
            rush_yds = row.xpath('./td[@data-stat="rush_yds"]/text()').extract_first()
            rush_yds_per_att = row.xpath('./td[@data-stat="rush_yds_per_att"]/text()').extract_first()
            rush_td = row.xpath('./td[@data-stat="rush_td"]/text()').extract_first()
            targets = row.xpath('./td[@data-stat="targets"]/text()').extract_first()
            rec = row.xpath('./td[@data-stat="rec"]/text()').extract_first()
            rec_yds = row.xpath('./td[@data-stat="rec_yds"]/text()').extract_first()
            rec_yds_per_rec = row.xpath('./td[@data-stat="rec_yds_per_rec"]/text()').extract_first()
            rec_td = row.xpath('./td[@data-stat="rec_td"]/text()').extract_first()
            fumbles = row.xpath('./td[@data-stat="fumbles"]/text()').extract_first()
            fumbles_lost = row.xpath('./td[@data-stat="fumbles_lost"]/text()').extract_first()
            all_td = row.xpath('./td[@data-stat="all_td"]/text()').extract_first()
            two_pt_md = row.xpath('./td[@data-stat="two_pt_md"]/text()').extract_first()
            two_pt_pass = row.xpath('./td[@data-stat="two_pt_pass"]/text()').extract_first()

            item = FantasyFootballAdpItem()
            item['player'] = player
            item['pos'] = pos
            item['age'] = age
            item['g'] = g
            item['gs'] = gs
            item['pass_cmp'] = pass_cmp
            item['pass_att'] = pass_att
            item['pass_yds'] = pass_yds
            item['pass_td'] = pass_td
            item['pass_int'] = pass_int
            item['rush_att'] = rush_att
            item['rush_yds'] = rush_yds
            item['rush_yds_per_att'] = rush_yds_per_att
            item['rush_td'] = rush_td
            item['targets'] = targets
            item['rec'] = rec
            item['rec_yds'] = rec_yds
            item['rec_yds_per_rec'] = rec_yds_per_rec
            item['rec_td'] = rec_td
            item['fumbles'] = fumbles
            item['fumbles_lost'] = fumbles_lost
            item['all_td'] = all_td
            item['two_pt_md'] = two_pt_md
            item['two_pt_pass'] = two_pt_pass

            yield item