
import json
import Scraper

scraper = Scraper.Scraper()
data = scraper.get_CC_subjects()
json.dump(data, open('subjects.json','w'))




