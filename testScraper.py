
import json
import Scraper

scraper = Scraper.Scraper()
data = scraper.get_CC_nav()
json.dump(data, open('temp_CC_nav.json','w'))




