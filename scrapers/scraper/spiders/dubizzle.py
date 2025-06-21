import re
import json
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scraper.items import DubizzleItem

class DubizzleSpider(CrawlSpider):
    name = "dubizzle"
    allowed_domains = ["dubizzle.sa"]
    start_urls = ["https://www.dubizzle.sa/en/vehicles/cars-for-sale/"]

    custom_settings = {
        'FEEDS': {
            'dubizzle.json': {'format': 'json', 'encoding': 'utf8', 'overwrite': True},
        },
        'COOKIES_ENABLED': True,
        'CONCURRENT_REQUESTS': 20,
        'DOWNLOAD_DELAY': 2,
        'RANDOMIZE_DOWNLOAD_DELAY': True,
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_START_DELAY': 0.5,
        'AUTOTHROTTLE_MAX_DELAY': 10,
        'AUTOTHROTTLE_TARGET_CONCURRENCY': 2.0,
        'RETRY_ENABLED': True,
        'RETRY_TIMES': 8,
        'RETRY_HTTP_CODES': [429,500,502,503,504,408],
        'DOWNLOAD_HANDLERS' : {
    "http": "scrapy_impersonate.ImpersonateDownloadHandler",
    "https": "scrapy_impersonate.ImpersonateDownloadHandler",
},
        'DOWNLOADER_MIDDLEWARES': {
        # scrapy-impersonate must go early, before other UA/header middleware
        #'scrapy_impersonate.middleware.ScrapyImpersonateMiddleware': 100,

        # you can keep FreeProxy + EmptyPageRetry as before
        #"scraper.middlewares.SwiftshadowProxyMiddleware": 300,
        'scraper.middlewares.FreeProxyMiddleware':          200,
        'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 210,
        'scraper.middlewares.EmptyPageRetryMiddleware':     300,

        # drop your old BrowserHeaderMiddleware / RandomUserAgentMiddleware
        'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': None,
        'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    },'IMPERSONATE_BROWSER': 'firefox-115',
    }

    rules = (
        Rule(LinkExtractor(allow=r'/en/vehicles/cars-for-sale/\?page=\d+'), follow=True),
        Rule(LinkExtractor(allow=r'/en/ad/'), callback='parse_ad', follow=False),
    )

    def parse_ad(self, response):
        item = DubizzleItem()
        item['url'] = response.url

        # — 1) JSON-LD —
        ld_txt = response.xpath('//script[@type="application/ld+json"]/text()').get()
        try:
            schema = json.loads(ld_txt) if ld_txt else {}
        except json.JSONDecodeError:
            schema = {}

        def to_int(v):
            try: return int(float(v))
            except: return None

        # map schema fields
        item['title']       = schema.get('name')
        item['description'] = schema.get('description')
        offers = schema.get('offers') or []



        offer = offers[0] if isinstance(offers, list) and offers else {}
        
        item['currency']    = offer.get('priceCurrency')
        od = schema.get('mileageFromOdometer') or {}
        item['kilometers']  = to_int(od.get('value'))
        item['brand']       = schema.get('brand')
        item['model']       = schema.get('model')
        item['year']        = schema.get('modelDate')
        imgs = schema.get('image')
        item['images']      = [imgs] if isinstance(imgs, str) else (imgs or [])

        # — 2) dataLayer via regex on full HTML —
        html = response.text
        m = re.search(
            r"window\['dataLayer'\]\.push\(\s*({.*?})\s*\);",
            html, flags=re.DOTALL
        )
        dl = {}
        if m:
            blob = m.group(1)
            # remove trailing commas
            blob = re.sub(r",\s*}", "}", blob)
            blob = re.sub(r",\s*]", "]", blob)
            try:
                dl = json.loads(blob)
            except json.JSONDecodeError:
                dl = {}

        # helper to pick first valid value
        def pick(*keys):
            for k in keys:
                v = dl.get(k)
                if v not in (None, "", []):
                    return v

        # map dataLayer fields
        item['price']             = pick('price')
        item['doors']             = pick('doors')
        item['seats']             = pick('seats')
        item['owners']            = pick('owners')
        item['color']             = pick('color')
        item['interior']          = pick('interior')
        item['air_con']           = pick('air_con')
        item['body_type']         = pick('body_type')
        item['new_used']          = pick('new_used')
        item['source']            = pick('source')
        item['transmission_type'] = pick('transmission_type', 'transmission')
        item['fuel_type']         = pick('fuel_type', 'petrol')

        # mileage fallback
        if not item.get('kilometers'):
            item['kilometers'] = to_int(pick('mileage'))

        # seller & location
        item['seller_type'] = pick('seller_type')
        item['location']    = pick('loc_name', 'loc_1_name', 'loc_2_name')

        yield item
