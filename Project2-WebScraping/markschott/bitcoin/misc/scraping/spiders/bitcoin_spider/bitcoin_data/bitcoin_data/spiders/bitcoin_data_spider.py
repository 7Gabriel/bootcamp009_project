from scrapy import Spider
from scrapy.selector import Selector
from bitcoin_data.items import BitcoinDataItem


class BitcoinDataSpider(Spider):
    name = "bitcoin_data_spider"
    allowed_urls = ['https://99bitcoins.com/']
    start_urls = ['https://99bitcoins.com/price-chart-history/']

    def verify(self, content):
		if isinstance(content, list):
			 if len(content) > 0:
				 content = content[0]
				 # convert unicode to str
				 return content.encode('ascii','ignore')
			 else:
				 return ""
                elif isinstance(content,type(None)):
                    return ""
		else:
			# convert unicode to str
			return content.encode('ascii','ignore')

    def parse(self, response):
       chart_data = response.xpath("//div[@class='post-content']/script/text()")
       prices = chart_data.extract()
#       prices = self.verify(prices)
       item = BitcoinDataItem()
       item['prices'] = prices
       yield prices
        
