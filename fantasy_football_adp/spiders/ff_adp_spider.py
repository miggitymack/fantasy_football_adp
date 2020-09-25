from scrapy import Spider, Request
from fantasy_football_adp.items import FantasyFootballAdpItem
import json


class TennisSpider(Spider):
    name = "tennis_spider"
    allowed_urls = ['https://www.pro-football-reference.com']
    start_urls = ['https://www.pro-football-reference.com/years/2018/fantasy.htm']

    def parse(self, response):
        player = response.xpath('//table/tbody/tr/td[@data-stat="player"]/a/text()').extract()[0]
        pos = response.xpath('//table/tbody/tr/td[@data-stat="fantasy_pos"]/text()').extract()[0]
        age = response.xpath('//table/tbody/tr/td[@data-stat="age"]/text()').extract()[0]
        g = response.xpath('//table/tbody/tr/td[@data-stat="g"]/text()').extract()[0]
        gs = response.xpath('//table/tbody/tr/td[@data-stat="gs"]/text()').extract()[0]
        pass_cmp = response.xpath('//table/tbody/tr/td[@data-stat="pass_cmp"]/text()').extract()[0]
        pass_att = response.xpath('//table/tbody/tr/td[@data-stat="pass_att"]/text()').extract()[0]
        pass_yds = response.xpath('//table/tbody/tr/td[@data-stat="pass_yds"]/text()').extract()[0]
        pass_td = response.xpath('//table/tbody/tr/td[@data-stat="pass_td"]/text()').extract()[0]
        pass_int = response.xpath('//table/tbody/tr/td[@data-stat="pass_int"]/text()').extract()[0]
        rush_att = response.xpath('//table/tbody/tr/td[@data-stat="rush_att"]/text()').extract()[0]
        rush_yds = response.xpath('//table/tbody/tr/td[@data-stat="rush_yds"]/text()').extract()[0]
        yds_per_att = response.xpath('//table/tbody/tr/td[@data-stat="yds_per_att"]/text()').extract()[0]
        rush_td = response.xpath('//table/tbody/tr/td[@data-stat="rush_td"]/text()').extract()[0]
        pass_targets = response.xpath('//table/tbody/tr/td[@data-stat="pass_targets"]/text()').extract()[0]
        rec = response.xpath('//table/tbody/tr/td[@data-stat="rec"]/text()').extract()[0]
        rec_yds = response.xpath('//table/tbody/tr/td[@data-stat="rec_yds"]/text()').extract()[0]
        rec_yds_per_rec = response.xpath('//table/tbody/tr/td[@data-stat="rec_yds_per_rec"]/text()').extract()[0]
        rec_td = response.xpath('//table/tbody/tr/td[@data-stat="rec_td"]/text()').extract()[0]
        fumbles = response.xpath('//table/tbody/tr/td[@data-stat="fumbles"]/text()').extract()[0]
        fumbles_lost = response.xpath('//table/tbody/tr/td[@data-stat="fumbles_lost"]/text()').extract()[0]
        all_td = response.xpath('//table/tbody/tr/td[@data-stat="all_td"]/text()').extract()[0]
        two_pt_md = response.xpath('//table/tbody/tr/td[@data-stat="two_pt_md"]/text()').extract()[0]
        two_pt_pass = response.xpath('//table/tbody/tr/td[@data-stat="two_pt_pass"]/text()').extract()[0]

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
        item['yds_per_att'] = yds_per_att
        item['rush_td'] = rush_td
        item['pass_targets'] = pass_targets
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