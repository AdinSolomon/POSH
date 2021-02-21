import json
import Scraper

scraper = Scraper.Scraper()
data = scraper.scrapeCC(
    term_lengths=["quarter"],
    degrees=["undergrad"],
    subjects=["CS"]
)
json.dump(data, open('temp_CC.json','w'))

