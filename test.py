
import json

import Scraper
#import CourseCatalog as CC
#import TermMasterSchedule as TMS

scraper = Scraper.Scraper()
data:dict = scraper.scrapeTermMasterSchedule(
    terms = ["Fall Quarter 20-21"],
    colleges = ["Col of Computing & Informatics"],
    subjects = ["CS"]
)
