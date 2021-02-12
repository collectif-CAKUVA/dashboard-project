from scraper_api import ScraperAPIClient
from config import *
client = ScraperAPIClient({token})
result = client.get(url={url}, render=True).text
print(result)

# Scrapy users can simply replace the urls in their start_urls and parse function
# Note for Scrapy, you should not use DOWNLOAD_DELAY and
# RANDOMIZE_DOWNLOAD_DELAY, these will lower your concurrency and are not
# needed with our API
# ...other scrapy setup code


