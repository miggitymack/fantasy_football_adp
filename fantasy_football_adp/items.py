# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FantasyFootballAdpItem(scrapy.Item):
    player = scrapy.Field()
    pos = scrapy.Field()
    age = scrapy.Field()
    g = scrapy.Field()
    gs = scrapy.Field()
    pass_cmp = scrapy.Field()
    pass_att = scrapy.Field()
    pass_yds = scrapy.Field()
    pass_td = scrapy.Field()
    pass_int = scrapy.Field()
    rush_att = scrapy.Field()
    rush_yds = scrapy.Field()
    rush_yds_per_att = scrapy.Field()
    rush_td = scrapy.Field()
    targets = scrapy.Field()
    rec = scrapy.Field()
    rec_yds = scrapy.Field()
    rec_yds_per_rec = scrapy.Field()
    rec_td = scrapy.Field()
    fumbles = scrapy.Field()
    fumbles_lost = scrapy.Field()
    all_td = scrapy.Field()
    two_pt_md = scrapy.Field()
    two_pt_pass = scrapy.Field()
