from tutorial.items import Item
import scrapy
from tutorial.items import WebcrawlerScrapyItem
class HuxiuSpider(scrapy.Spider):
    name = "huxiu"
    start_urls = ["https://www.imooc.com/course/list?page=" + str(x) for x in range(1, 5, 1)]
            
    def parse(self, response):
      page = response.url.split("/")[-2]
      filename = '2.html'
      titles = response.xpath('//h3[@class="course-card-name"]/text()').extract()
      degrees = response.xpath('//div[@class="course-card-info"]/span[1]/text()').extract()
      counts = response.xpath('//div[@class="course-card-info"]/span[2]/text()').extract()
      desc= response.xpath('//p[@class="course-card-desc"]/text()').extract()
      with open (filename,'ab') as f :
          for (title,degree,des) in zip(titles,degrees,desc):
            # title = str.encode(title+"  "+degree+"  "+des+'\n')
            # f.write(title)
            Item = WebcrawlerScrapyItem()
            Item["title"]=title
            Item["degree"]=degree
            Item["desc"]=des
            yield Item 
            print (Item)