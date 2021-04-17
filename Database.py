
import os
import json
import datetime
from selenium import webdriver

import Scraper
import CourseCatalog as CC
import TermMasterSchedule as TMS
from util.file_system import make_path
from util.exceptions import InvalidSubject, NoColleges

datetime_format = "%Y-%m-%d %H:%M:%S"

repo_dir = __file__.replace("Database.py","")
database_dir = make_path(repo_dir, "Database")
subjects_dir = make_path(database_dir, "Subjects")
navigation_dir = make_path(database_dir, "Navigation")
error_dir = make_path(database_dir, 'Errors')
misc_dir = make_path(database_dir, 'Misc')
os.makedirs(database_dir, exist_ok=True)
os.makedirs(subjects_dir, exist_ok=True)
os.makedirs(navigation_dir, exist_ok=True)
os.makedirs(error_dir, exist_ok=True)
os.makedirs(misc_dir, exist_ok=True)

def update_navigation() -> None:
    scraper = Scraper.Scraper()
    nav_data = scraper.get_all_nav()
    # Subject Names
    json.dump(nav_data["subject_names"], open(make_path(navigation_dir, 'subject_names.json'),'w'))
    # Subject -> Colleges
    json.dump(nav_data["subject_colleges"], open(make_path(navigation_dir, 'subject_colleges.json'),'w'))
    # College -> Subjects
    json.dump(nav_data["college_subjects"], open(make_path(navigation_dir, 'college_subjects.json'),'w'))
    # Errors
    json.dump(nav_data["errors"], open(make_path(error_dir, 'update_nav.json'),'w'))

def update_subject(subject_code:str) -> None:
    subject_colleges = json.load(open(make_path(navigation_dir, "subject_colleges.json")))
    colleges = None
    if not (colleges := subject_colleges.get(subject_code, None)):
        raise InvalidSubject(f"The subject code {subject_code} was not found in subject_colleges.json")
    if not (colleges := colleges["TMS"]):
        raise NoColleges(f"The subject code {subject_code} has not TMS entry")

    scraper = Scraper.Scraper()
    data = {
        "Subject Code" : subject_code,
        "Subject Names" : json.load(open(make_path(navigation_dir, 'subject_names.json')))[subject_code],
        "Last Updated" : datetime.datetime.now().strftime(datetime_format),
        "Courses" : scraper.scrapeCC(term_lengths=CC.TermLengths, degrees=CC.Degrees, subjects=[subject_code])[subject_code]
    }
    tms_data = scraper.scrapeTMS(terms=TMS.Quarters, colleges=colleges, subjects=[subject_code])
    try:
        for course_number, course_offerings in tms_data[subject_code].items():
            data["Courses"][course_number]["Offerings"] = course_offerings
    except KeyError as e:
        json.dump(tms_data, open('tms_data_error.json', 'w'))
        raise e
    json.dump(data, open(make_path(subjects_dir, f"{subject_code}.json"), 'w'))
    

