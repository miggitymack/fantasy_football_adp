# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FantasyFootballAdpItem(scrapy.Item):
    position = scrapy.Field()
    age = scrapy.Field()
    games = scrapy.Field()
    games_started = scrapy.Field()
    pass_completed = scrapy.Field()
    pass_attempted = scrapy.Field()
    pass_yards = scrapy.Field()
    pass_tds = scrapy.Field()
    int = scrapy.Field()
    rush_att = scrapy.Field()
    rush_yds = scrapy.Field()
    yds_per_att = scrapy.Field()
    rush_tds = scrapy.Field()
    pass_targets = scrapy.Field()
    rec = scrapy.Field()
    rec_yards = scrapy.Field()
    yards_per_rec = scrapy.Field()
    rec_tds = scrapy.Field()
    fumbles = scrapy.Field()
    fumbles_lost = scrapy.Field()
    total_tds = scrapy.Field()
    two_pt_conv_made = scrapy.Field()
    two_pt_conv_pass = scrapy.Field()
