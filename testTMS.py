
import json

import Scraper
#import CourseCatalog as CC
from TermMasterSchedule import Quarters

scraper = Scraper.Scraper()
data:dict = scraper.scrapeTMS(
    terms = ["Fall Quarter 20-21"],
    colleges = ["Arts and Sciences"],
    subjects = ["GEO"]
)
assert (len(data) != 0), "No data was found!"
json.dump(data, open('temp_TMS.json','w'))

