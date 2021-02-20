
import json

import Scraper
#import CourseCatalog as CC
from TermMasterSchedule import Quarters

scraper = Scraper.Scraper()
json.dump(scraper.get_TMS_subjects(), open('temp.json','w'))

#data:dict = scraper.scrapeTMS(
#    terms = Quarters,
#    colleges = ["Col of Computing & Informatics"],
#    subjects = ["CS"]
#)
#json.dump(data, open('temp.json','w'))

