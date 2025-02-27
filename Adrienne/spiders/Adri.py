import scrapy
from datetime import datetime
from calendar import monthrange
import json
import pandas as pd

class AdriSpider(scrapy.Spider):
    name = "Adri"
    List = []
    
    proxy = 'http://private.residential.proxyrack.net:10025'
    username = 'lew_soft;country=US'
    password = 'AQZ3OLF-9E2DHMO-7CNYVIZ-NKIKJCJ-DP301FJ-GJEYVYL-YDOPMPH'
    port = 10025
    superProxyUrl = ('http://%s:%s@private.residential.proxyrack.net:%d' %(username,password, port))
    
    def generate_month_urls(self, year):
        month_urls = []
        for month in range(1, 13):
            start_date = f"{year}-{month:02d}-01"
            end_day = monthrange(year, month)[1]
            end_date = f"{year}-{month:02d}-{end_day}"
            url = f"https://www.arshtcenter.org/ace-api/events?startDate={start_date}&endDate={end_date}"
            month_urls.append(url)
        return month_urls

    def start_requests(self, response=None):
        current_year = datetime.now().year
        for url in self.generate_month_urls(current_year):
            yield scrapy.Request(url=url, callback=self.parse,meta={'proxy':self.superProxyUrl})

    def parse(self, response):
        print(response.body)
        # jsondata = json.loads(response.body)
        # print(jsondata)
        # jsondata = response.body
        # print(jsondata)
    #     for element in jsondata:
    #         EventName = element.get("name").strip()
    #         EventDate = element["eventDate"]
    #         Id = element["id"]
    #         FacilityId = element["facilityId"]
    #         performanceid = element["productionSeasonId"]
    #         BuyTicketUrl = element["buyTicketCtaUrl"]
    #         if not BuyTicketUrl.startswith("http"):
    #             BaseUrl = "https://www.arshtcenter.org"
    #             BuyTicketUrl = f"{BaseUrl}{BuyTicketUrl}"
    #             yield scrapy.Request(BuyTicketUrl, callback=self.parse_link, meta={"EventName": EventName, "EventDate": EventDate, "Id": Id, "FacilityId": FacilityId})
    #         else:
    #             yield scrapy.Request(BuyTicketUrl, callback=self.parse_link, meta={"EventName": EventName, "EventDate": EventDate, "Id": Id, "FacilityId": FacilityId})

    # def parse_link(self, response):
    #     EventName = response.meta["EventName"]
    #     EventDate = response.meta["EventDate"]
    #     print(f"EventName:{EventName}")
        # Id = response.meta["Id"]
        # FacilityId = response.meta["FacilityId"]
        # ResponsePath = response.xpath("//ul[@class = 'stack-sm ace-bestavailable-ticketamount']/li/div/div[1]")
        # for data in ResponsePath:
        #     category = data.xpath(".//p[1]/text()").get().strip()
        #     Price = data.xpath(".//p[2]/text()").get()
        #     SoldOut = data.xpath(".//p[3]/text()").get() if data.xpath(".//p[3]/text()") else None
        #     if SoldOut != "Sold Out":
        #         event = {
        #             "EventName": EventName,
        #             "EventDate": EventDate,
        #             "Id": Id,
        #             "Category": category,
        #             "Price": Price,
        #         }
        #         self.List.append(event)
        # df = pd.DataFrame(self.List)
        # df.to_csv("data.csv", index=False)
