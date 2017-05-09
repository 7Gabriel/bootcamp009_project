from scrapy import Spider
from scrapy.selector import Selector
from bitcoin.items import BitcoinItem


class BitcoinSpider(Spider):
    name = "bitcoin_spider"
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
       # chart_data = response.xpath("//div[@class='post-content']/script/text()")
       # prices = chart_data.extract()
       # yield prices
        
        rows = response.xpath("//div[@class='post-content']//div[@class='bitcoin_history']")
        sz = len(rows)
        for i in range(sz):
            event_no = str(sz - i)
            title = rows[i].xpath('./h3/text()').extract_first()
            val = rows[i].xpath('./div/span[2]/text()').extract_first()
            val_after_10days = rows[i].xpath('./div/span[4]/text()').extract_first()            
            story = rows[i].xpath('./p/text()').extract()
            sources = rows[i].xpath('./p/a/text()').extract()

            event_no = self.verify(event_no)
            title = self.verify(title)
            val = self.verify(val)
            val_after_10days = self.verify(val_after_10days)
            story = self.verify(story)
            sources = self.verify(sources)

            item = BitcoinItem()
            item['event_no'] = event_no
            item['title'] = title
            item['val'] = val
            item['val_after_10days'] = val_after_10days
            item['story'] = story
            item['sources'] = sources            

            yield item
