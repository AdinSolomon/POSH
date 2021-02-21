
import re
import json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import CourseCatalog as CC
import TermMasterSchedule as TMS
import util.web as web
from util.general import dict_deepupdate
from util.exceptions import UnsupportedBrowser

major_symbol_regex = r"\(([A-Z-]{2,})\)"
college_symbol_regex = r"\(([A-Z)]{,2})\)"

class Scraper:
    def __init__(self, browser:str = "Chrome"):
        self.browser = browser
        self.driver = None
        self.urls = []
    def __del__(self):
        self.stop()
    # Driver Managers
    def is_started(self):
        return self.driver != None
    def start(self, started_ok:bool = False) -> None:
        # Make sure the previous session is closed
        if started_ok and self.is_started():
            return
        else:
            self.stop()
        # Switch on the browser
        if self.browser == "Chrome":
            self.driver = webdriver.Chrome()
        else:
            raise UnsupportedBrowser("Chrome is the only supported browser as of now")
    def stop(self):
        if self.is_started():
            self.driver.close()
            self.driver = None
    def driver_url_put(self):
        if self.is_started():
            self.urls.append(self.driver.current_url)
        else:
            self.start()
    def driver_url_pop(self):
        assert (self.is_started()), "Driver was not on when driver_url_pop was called"
        if len(self.urls) > 0:
            self.driver.get(self.urls.pop(0))
        else:
            self.stop()
    # Scrape Navigation Data
    def get_CC_nav(self) -> dict:
        self.start()
        errors = {}
        subject_names = {}
        subject_colleges = {}
        college_subjects = {}
        for url in CC.URLs:
            self.driver.get(url)
            Columns = self.driver.find_elements_by_class_name("qugcourses")
            for column in Columns:
                for elem in column.find_elements_by_xpath(".//*"):
                    if elem.tag_name == "h2": # College element
                        college = elem.text
                        if college not in college_subjects:
                            college_subjects[college] = []
                    elif elem.tag_name == "a": # Subject element
                        subject_code = re.findall(major_symbol_regex, elem.text)[0]
                        subject_name = elem.text.replace(f"({subject_code})","").strip()
                        # Record subject code -> subject name
                        subject_names[subject_code] = subject_name
                        # Record subject code -> colleges
                        if subject_code not in subject_colleges:
                            subject_colleges[subject_code] = []
                        if college not in subject_colleges[subject_code]:
                            subject_colleges[subject_code].append(college)
                        # Record college -> subject codes
                        if subject_code not in college_subjects[college]:
                            college_subjects[college].append(subject_code)
                    else:
                        if "element_tags" not in errors:
                            errors["element_tags"] = []
                        if elem.tag_name not in errors["element_tags"]:
                            errors["element_tags"].append(elem.tag_name)
        return {
            'subject_names' : subject_names,
            'college_subjects' : college_subjects,
            'subject_colleges' : subject_colleges,
            'errors' : errors
        }
    def get_TMS_nav(self) -> dict:
        self.start()
        self.driver.get(TMS.HomePage)
        errors = {}
        subject_names = {}
        subject_colleges = {}
        college_subjects = {}
        for term in TMS.Terms:
            try:
                self.driver.find_element_by_link_text(term).click()
            except:
                errors["Terms"] = errors.get("Terms",[]) + [term]
                continue
            for college in list(elem.text for elem in self.driver.find_elements_by_xpath("/html/body/table/tbody/tr[2]/td/table[2]/tbody/tr[4]/td/div/a")):
                if college not in college_subjects:
                    college_subjects[college] = []
                self.driver.find_element_by_link_text(college).click()
                for subject_link in (self.driver.find_elements_by_class_name("odd") + self.driver.find_elements_by_class_name("even")):
                    subject_code = re.findall(major_symbol_regex, subject_link.text)[0].upper()
                    subject_name = subject_link.text.replace(f"({subject_code})","").strip()
                    # Record subject code -> subject name
                    subject_names[subject_code] = subject_name
                    # Record subject_code -> colleges
                    if subject_code not in subject_colleges:
                        subject_colleges[subject_code] = []
                    if college not in subject_colleges[subject_code]:
                        subject_colleges[subject_code].append(college)
                    # Record college -> subject code
                    if subject_code not in college_subjects[college]:
                        college_subjects[college].append(subject_code)
                self.driver.back()
            self.driver.back()
        self.stop()
        return {
            'subject_names' : subject_names,
            'college_subjects' : college_subjects,
            'subject_colleges' : subject_colleges,
            'errors' : errors
        }
    def get_all_nav(self) -> dict:
        CC_data = self.get_CC_nav()
        TMS_data = self.get_TMS_nav()
        # Subject Names
        subject_names = {subject : {"CC" : name} for subject, name in CC_data["subject_names"].items()}
        dict_deepupdate(subject_names, {subject : {"TMS" : name} for subject, name in TMS_data["subject_names"].items()})
        for v in subject_names.values():
            if "CC" not in v:
                v["CC"] = None
            if "TMS" not in v:
                v["TMS"] = None
        # Subject -> Colleges
        subject_colleges = {subject : {"CC" : colleges} for subject, colleges in CC_data["subject_colleges"].items()}
        dict_deepupdate(subject_colleges, {subject : {"TMS" : colleges} for subject, colleges in TMS_data["subject_colleges"].items()})
        for v in subject_colleges.values():
            if "CC" not in v:
                v["CC"] = None
            if "TMS" not in v:
                v["TMS"] = None
        # College -> Subjects
        college_subjects = {college : {"CC" : subjects} for college, subjects in CC_data["college_subjects"].items()}
        dict_deepupdate(college_subjects, {college : {"TMS" : subjects} for college, subjects in TMS_data["college_subjects"].items()})
        for v in college_subjects.values():
            if "CC" not in v:
                v["CC"] = None
            if "TMS" not in v:
                v["TMS"] = None
        # Errors (i guess)
        errors = CC_data["errors"]
        errors.update(TMS_data["errors"])
        return {
            "subject_names" : subject_names,
            "subject_colleges" : subject_colleges,
            "college_subjects" : college_subjects,
            "errors" : errors
        }
    # Scrape Subject/Course Data
    def scrapeCC(self, 
        term_lengths:list = [],
        degrees:list      = [],
       #colleges:list     = [],
        subjects:list     = []) -> dict:
        # TODO - Add support for college selection
        # Returns a dictionary mapping from subject symbol to course data
        #   ex.   { "CS" : { "150" : ... } }
        # If any parameters are [], it is assumed that the user is already at a page designating
        # the desired parameter. For example, if term_length=[], then self.driver.current_url is
        # parsed for the term length and scraping will commence accordingly.
        self.driver_url_put()
        
        def _scrape() -> dict:
            courses = {}
            for elem in self.driver.find_elements_by_class_name("courseblock"):
                lines = elem.text.split("\n")
                title_line = lines[0].split(" ")
                course_number = title_line[1] # " ".join(title_line[:2]) gives 'CS 150' instead of '150'
                courses[course_number] = {}
                courses[course_number]["Name"] = " ".join(title_line[2:-2])
                courses[course_number]["Credits"] = title_line[-2]
                courses[course_number]["Description"] = lines[1]
                for line in lines[2:]:
                    key = line.split(':')[0]
                    val = line.replace(key+':', "").strip()
                    courses[course_number][key] = val
            return courses
        def _make_urls() -> list:
            urls:list = []
            # first use term_lengths
            if term_lengths == []:
                # the driver is already at the page of the desired term length
                current_url = self.driver.current_url
                assert (CC.HomePage in current_url), "Not at the course catalog!"
                current_length = current_url.split(web.SEP)[4]
                assert (current_length in CC.TermLengths), "Not at a valid term length in the course catalog!"
                urls = [web.make_url(CC.HomePage, current_length)]
            else:
                assert (set(term_lengths).issubset(set(CC.TermLengths))), "One of your term lengths is not valid!"
                urls = [CC.HomePage + length for length in term_lengths]
            if degrees == []:
                # the driver is already at the page of the desired degree level
                current_url = self.driver.current_url
                assert (CC.HomePage in current_url), "Not at the course catalog!"
                current_degree = current_url.split(web.SEP)[5]
                assert (current_degree in CC.Degrees), "Not at a valid degree in the course catalog!"
                urls = [web.make_url(url, current_degree) for url in urls]
            else:
                assert (set(degrees).issubset(set(CC.Degrees))), "One of your degrees is not valid!"
                urls = sum([[web.make_url(url, degree) for degree in degrees] for url in urls], [])
            return urls
        def _subjects(subjects:[str] = subjects):
            for subject in subjects:
                yield subject.upper()

        # if there are no arguments, assume that the driver is already at the page to scrape
        if term_lengths == None and degrees == None and subjects == None:
            assert (CC.HomePage in (current_url := self.driver.current_url)), "Not at the course catalog!"
            assert (len(thingies := current_url.split(web.SEP)) == 8), "Not at a subject's page in the course catalog!"
            l, g, s = thingies[4:7]
            assert (l in CC.TermLengths), "term length is not valid!"
            assert (g in CC.Degrees), "degree is not valid!"
            assert (len(s) <= 2), "subject is not valid!"
            return { s : _scrape() }

        # For each url (constructed from term_lengths and degrees):
        #   for each subject in subjects that's on the page:
        #      add ya boi to the dictionary to be returned!
        
        # compile the list of length/degree urls first
        urls = _make_urls()

        # while urls can be generated using the subject symbol, a length/degree
        # page might not have that subject so the url may be invalid. Therefore,
        # each time a subject is queried, the length/degree page is searched for
        # the link corresponding to that subject.

        data = {} # { "CS" : {"150": {...}, ... }, ... }
        failed_finds = {"origin":"scrapeCourseCatalog()"}
        for url in urls:
            self.driver.get(url)
            for subject in _subjects():
                try:
                    elem = self.driver.find_element_by_partial_link_text("({0})".format(subject))
                    elem.click()
                    if subject not in data:
                        data[subject] = {}
                    dict_deepupdate(data[subject], _scrape())
                    self.driver.back()
                except NoSuchElementException:
                    failed_finds[self.driver.current_url] = [subject] + \
                        failed_finds.get(self.driver.current_url, [])
        # Keep failed finds in case someone wants them
        with open("C:\\Users\\adinb\\Documents\\Personal\\Projects\\POSH\\temp_failed_finds.json", "w") as f:
            json.dump(failed_finds, f)
        
        # Return to where the driver was when this function was called
        self.driver_url_pop()

        return data
    def scrapeTMS(self,
        terms:list    = [], 
        colleges:list = [],
        subjects:list = []) -> dict:
        # Returns a dictionary mapping from subject symbol to course data
        #   ex.   { "CS" : { "150" : { "Fall Quarter 20-21" : { "Section01" : {...} } } } }
        # If any parameters are [], it is assumed that the user is already at a page designating
        # the desired parameter. For example, if term_length=[], then self.driver.current_url is
        # parsed for the term length and scraping will commence accordingly.

        # This function is more complicated that scrapeCourseCatalog() because the ultimate
        # formatting for the return dictionary is more similar to the structure of the 
        # course catalog. TMS is wacky because it's organized like term/college/subject
        # instead of subject/course_number/offerings

        # Return to the driver's starting location after scraping
        self.driver_url_put()

        def _scrape() -> dict:
            # Returns a dictionary mapping from course number to sections
            #   ex. { "150" : { "Section01" : {...} } }
            def _parse_course(lines:[str]) -> dict:
                # returns a dictionary { "150"" : { "Section01" : {...} } }
                course_number:str = (tr := lines[0].split())[1]
                section_id:str = tr[-1]
                section_info:dict = {
                    "Format/Style" : ' '.join(tr[2:-1]),
                    "CRN"          : lines[1],
                   #"Name"         : lines[2],
                    "Schedule"     : " | ".join(lines[3:-1]),
                    "Professor"    : lines[-1]
                }
                return { course_number : { section_id : section_info} }
            table_data = self.driver.find_element_by_xpath(TMS.xpath_to_course_table).text.split('\n')
            assert (len(table_data) > 0), "Data was not scraped properly"
            code = table_data[1].split()[0]
            count = 0
            courses = {} # { "150" : { "Section01" : {...} } }
            current_section = []
            # TODO - make this into a cool generator function
            for line in table_data[1:]: # The first line is the table header
                if code in line and count > 3: # to allow for course title with the code in it
                    # A complete section has been collected
                    dict_deepupdate(courses, _parse_course(current_section))
                    # Start loading another section
                    count = 1
                    current_section = [line]
                else:
                    count += 1
                    current_section.append(line)
            # The last course was loaded and still needs processing
            dict_deepupdate(courses, _parse_course(current_section))
            return courses
        def _subjects(subjects:[str] = subjects):
            for subject in subjects:
                yield subject.upper()

        # For each term (click on link)
        #   For each college (click on link)
        #       For each major (click on link)
        #           scrape ya boi
        #           go back
        #   go back
        # TODO - implement the no_arg default navigations
        data = {} # { "CS" : { "150": { "Fall Quarter 20-21" : { "Section01" : {...} } } } }
        failed_finds = {"origin":"scrapeTermMasterSchedule()"}
        self.driver.get(TMS.HomePage)
        for term in terms:
            try:
                self.driver.find_element_by_link_text(term).click()
                for college in colleges:
                    try:
                        self.driver.find_element_by_link_text(college).click()
                        for subject in _subjects():
                            try:
                                self.driver.find_element_by_partial_link_text(f"({subject})").click()
                                scraped_data = _scrape() # { "150" : { "Section01" : {...} } }
                                if subject not in data:
                                    data[subject] = {}
                                for course_number, sections in scraped_data.items():
                                    if not data[subject].get(course_number):
                                        data[subject][course_number] = {}
                                    if not data[subject][course_number].get(term):
                                        data[subject][course_number][term] = {}
                                    for section_id, section_data in sections.items():
                                        data[subject][course_number][term][section_id] = section_data
                                self.driver.back() 
                            except NoSuchElementException:
                                failed_finds[f"/{term}/{college}/"] = [subject] + \
                                    failed_finds.get(f"/{term}/{college}/", [])
                        self.driver.back()
                    except NoSuchElementException:
                        failed_finds[f"/{term}/"] = [college] + \
                            failed_finds.get(f"/{term}/", [])
                self.driver.back()
            except NoSuchElementException: # Finding the term failed
                failed_finds["/"] = [term] + \
                    failed_finds.get("/", [])
        # In case anyone wants these...
        with open("C:\\Users\\adinb\\Documents\\Personal\\Projects\\POSH\\temp_failed_finds.json", "w") as f:
            json.dump(failed_finds, f)

        # Return to the driver's starting location
        self.driver_url_pop()

        # Don't forget this part!
        return data
    
