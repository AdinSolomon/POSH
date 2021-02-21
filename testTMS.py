
import json

import Scraper
#import CourseCatalog as CC
from TermMasterSchedule import Quarters

scraper = Scraper.Scraper()
data:dict = scraper.scrapeTMS(
    terms = Quarters,
    colleges = ["Col of Computing & Informatics"],
    subjects = ["CS"]
)
json.dump(data, open('temp_TMS.json','w'))

