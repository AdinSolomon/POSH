
import re
import json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import CourseCatalog as CC
import TermMasterSchedule as TMS
from util import dict_deepupdate # TODO - fix the scrape functions update usage

SEP = '/'

def make_url(a:str, b:str, sep:str = SEP) -> str:
    return a + (sep if a[-1] != sep else "") + b
def make_url2(parts:list, sep:str = SEP) -> str:
    url = parts.pop(0)
    for part in parts:
        url += (sep if url[-1] != sep else "") + part
    return url

class Scraper:
    def __init__(self, browser:str = "Chrome"):
        self.browser = browser
        self.driver = None
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
            print("Chrome is the only browser supported right now! Driver has not been started.")
    def stop(self):
        if self.is_started():
            self.driver.close()
            self.driver = None
    # Scraping Functions
    def get_all_subjects(self) -> dict:
        # returns a dictionary mapping subject codes to subject
        # names as they appear in the course catalog
        self.start()
        self.driver.get(CC.HomePage)
        urls = sum([[make_url2([CC.HomePage,term_length,degree])
                        for degree in CC.Degrees] 
                            for term_length in CC.TermLengths],[])
        subjects = {}
        for url in urls:
            self.driver.get(url)
            for elem in self.driver.find_elements_by_xpath(
            "/html/body/div[@id='wrapper']/div[@id='content_wrapper']/div/div/div/div/div/a"):
                try:
                    subject_code = re.findall(CC.major_symbol_regex, elem.text)[0]
                except:
                    print(elem.text)
                subject_name = elem.text.replace(f"({subject_code})","").strip()
                subjects[subject_code] = subject_name
        self.stop()
        return subjects
    def get_all_colleges(self) -> dict:
        # TODO - this!
        # Maybe get these from TMS? Could get them from CC and also get the codes nobody cares about!
        pass
    def scrapeCourseCatalog(self, 
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
        origin = None
        if self.is_started():
            origin = self.driver.current_url
        self.start(started_ok = True)
        
        def _scrape() -> dict:
            courses = {}
            for elem in self.driver.find_elements_by_class_name("courseblock"):
                lines = elem.text.split("\n")
                title_line = lines[0].split(" ")
                course_number = title_line[1] # " ".join(title_line[:2]) gives 'CS 150' instead of '150'
                courses[course_number] = {}
                courses[course_number]["name"] = " ".join(title_line[2:-2])
                courses[course_number]["credits"] = title_line[-2]
                courses[course_number]["description"] = lines[1]
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
                current_length = current_url.split(SEP)[4]
                assert (current_length in CC.TermLengths), "Not at a valid term length in the course catalog!"
                urls = [make_url(CC.HomePage, current_length)]
            else:
                assert (set(term_lengths).issubset(set(CC.TermLengths))), "One of your term lengths is not valid!"
                urls = [CC.HomePage + length for length in term_lengths]
            if degrees == []:
                # the driver is already at the page of the desired degree level
                current_url = self.driver.current_url
                assert (CC.HomePage in current_url), "Not at the course catalog!"
                current_degree = current_url.split(SEP)[5]
                assert (current_degree in CC.Degrees), "Not at a valid degree in the course catalog!"
                urls = [url + degree for url in urls]
            else:
                assert (set(degrees).issubset(set(CC.Degrees))), "One of your degrees is not valid!"
                urls = sum([[make_url(url, degree) for degree in degrees] for url in urls], [])
            return urls
        def _subjects(subjects:[str] = subjects):
            for subject in subjects:
                yield subject.upper()

        # if there are no arguments, assume that the driver is already at the page to scrape
        if term_lengths == None and degrees == None and subjects == None:
            assert (CC.HomePage in (current_url := self.driver.current_url)), "Not at the course catalog!"
            assert (len(things := current_url.split(SEP)) == 8), "Not at a subject's page in the course catalog!"
            l, g, s = thingies[4:7]
            assert (l in CC.TermLength), "term length is not valid!"
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
                    dict_deepupdate(data[subject], _scrape())
                    self.driver.back()
                except NoSuchElementException:
                    failed_finds[self.driver.current_url] = [subject] + \
                        failed_finds.get(self.driver.current_url, [])
        # Keep failed finds in case someone wants them
        with open("C:\\Users\\adinb\\Documents\\Projects\\POSH\\temp_failed_finds.json", "w") as f:
            json.dump(failed_finds, f)
        
        # Return to where the driver was when this function was called
        if origin:
            self.driver.get(origin)
        else:
            self.stop()

        return data
    def scrapeTermMasterSchedule(self,
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
        origin = None
        if self.is_started():
            origin = self.driver.current_url
        self.start(started_ok = True)

        def _scrape() -> dict:
            # Returns a dictionary mapping from course number to sections
            #   ex. { "150" : { "Section01" : {...} } }
            def _parse_course(lines:[str]) -> dict:
                # returns a dictionary { "150"" : { "Section01" : {...} } }
                course_number:str = (tr := lines[0].split())[1]
                section_id:str = tr[-1]
                section_info:dict = {
                    "format"    : None, # TODO - this is a little more complicated
                    "style"     : None, # TODO - same with this boi
                    "CRN"       : lines[1],
                    "name"      : lines[2],
                    "schedule"  : '\n'.join(lines[3:-1]),
                    "professor" : lines[-1]
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
                    curent_section = [line]
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
            print(term)
            try:
                self.driver.find_element_by_link_text(term).click()
                for college in colleges:
                    print(college)
                    try:
                        self.driver.find_element_by_link_text(college).click()
                        for subject in _subjects():
                            print(subject)
                            try:
                                self.driver.find_element_by_partial_link_text(f"({subject})").click()
                                # This is getting complicated...
                                scraped_data = _scrape() # { "150" : { "Section01" : {...} } }
                                new_data = {subject : {}} # similar to data for update()
                                for course_number, section_data in scraped_data.items():
                                    #json.dump(scraped_data, open('temp.json','w'))
                                    section_id = [*section_data.keys()][0]
                                    section_data = [*section_data.values()][0]
                                    new_data[subject][course_number] = {}
                                    new_data[subject][course_number][term] = {}
                                    new_data[subject][course_number][term][section_id] = section_data
                                dict_deepupdate(data, new_data)
                                self.driver.back() 
                            except NoSuchElementException:
                                failed_finds[f"/{term}/{college}/"] = [subject] + \
                                    failed_finds.get(f"/{term}/{college}/", [])
                    except NoSuchElementException:
                        failed_finds[f"/{term}/"] = [college] + \
                            failed_finds.get(f"/{term}/", [])
            except NoSuchElementException: # Finding the term failed
                failed_finds["/"] = [term] + \
                    failed_finds.get("/", [])
        # In case anyone wants these...
        with open("C:\\Users\\adinb\\Documents\\Projects\\POSH\\temp_failed_finds.json", "w") as f:
            json.dump(failed_finds, f)

        # Return to the driver's starting location
        if origin:
            self.driver.get(origin)
        else:
            self.stop()

        # Don't forget this part!
        return data
        
