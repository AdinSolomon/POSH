
import re
from typing import Union
from selenium import webdriver, WebDriver
import CourseCatalog as CC
import TermMasterSchedule as TMS

SEP = '/'
def url_cat(a:str, b:str) -> str:
    return a + (SEP if a[-1] != SEP else "") + b

class Scraper:
    def __init__(self, browser:str = "Chrome"):
        self.driver = None
        if browser == "Chrome":
            self.driver = webdriver.Chrome()
        else:
            print("Browsers other than Chrome aren't supported rn...")
            exit()
    
    # TODO - compare the subjects parameter with a master list of all subjects
    def scrapeCatalog(self, term_lengths = [],
                            degrees      = [],
                           #colleges     = [],
                            subjects     = []) -> dict:
        # returns a dictionary mapping from subject symbol to course data
        # ex.   { "CS" : { "CS 150" : ... } }
        
        def _scrape(self) -> dict:
            courses = {}
            for elem in self.driver.find_elements_by_class_name("courseblock")[:5]:
                lines = elem.text.split("\n")
                title_line = lines[0].split(" ")
                course_number = " ".join(title_line[:2])
                courses[course_number] = {}
                courses[course_number]["name"] = " ".join(title_line[2:-2])
                courses[course_number]["credits"] = title_line[-2]
                courses[course_number]["description"] = lines[1]
                for line in lines[2:]:
                    key = line.split(':')[0]
                    val = line.replace(key+':', "").strip()
                    courses[course_number][key] = val
            return courses
        def _make_urls(self) -> list:
            urls:list = []
            # first use term_lengths
            if term_lengths == []:
                # the driver is already at the desired term length
                current_url = self.driver.current_url
                assert (CC.HomePage in current_url), "Not at the course catalog!"
                current_length = current_url.split(SEP)[4]
                assert (current_length in CC.TermLengths), "Not at a valid term length in the course catalog!"
                urls = [url_cat(CC.HomePage, current_length)]
            else:
                assert (term_lengths.issubset(CC.TermLengths)), "One of your term lengths is not valid!"
                urls = [CC.HomePage + length for length in term_lengths]
            if degrees == []:
                # the driver is already at the desired degree level
                current_url = self.driver.current_url
                assert (CC.HomePage in current_url), "Not at the course catalog!"
                current_degree = current_url.split(SEP)[5]
                assert (current_degree in CC.Degrees), "Not at a valid degree in the course catalog!"
                urls = [url + degree for url in urls]
            else:
                assert (degrees.issubset(CC.Degrees)), "One of your degrees is not valid!"
                urls = sum([[url_cat(url, degree) for degree in degrees] for url in urls], [])
            return urls
        
        # if there are no arguments, assume that the driver is already at the page to scrape
        if term_lengths == None and degrees == None and subjects == None:
            assert (CC.HomePage in (current_url := self.driver.current_url)), "Not at the course catalog!"
            assert (len(things := current_url.split(SEP)) == 8), "Not at a subject's page in the course catalog!"
            l, g, s = thingies[4:7]
            assert (l in CC.TermLength), "term length is not valid!"
            assert (g in CC.Degrees), "degree is not valid!"
            assert (len(s) <= 2), "subject is not valid!"
            return { s.upper() : _scrape() }

        # For each url (constructed from term_lengths and degrees):
        #   for each subject in subjects that's on the page:
        #      add ya boi to the dictionary to be returned!6
        
        # compile the list of length/degree urls first
        urls = _make_urls()

        # while urls can be generated using the subject symbol, a length/degree
        # page might not have that subject so the url may be invalid. Therefore,
        # each time a subject is queried, the length/degree page is searched for
        # the link corresponding to that subject.

        # compile the list of subject symbols
        # TODO - this! for now assume the list is all valid

        data = {}
        for url in urls:
            self.driver.get(url)
            for subject in subjects:
                # assume that the link is there but TODO add try/except for the error
                elem = self.driver.find_element_by_link_text("({0})".format(subject.upper()))
                elem.click()
                data[subject.upper()] = _scrape()
        return data
            


                
        
        
        
        







        # construct the urls
        urls = []
        # first add term lengths
        if type(term_length) == str:
            urls.append(CC.HomePage + term_length + '/')
        if type(term_length) == list:
            for l in term_length:
                urls.append(CC.HomePage + l + '/')
        if type(term_length) == None:
            for l in CC.TermLengths:
                urls.append(CC.HomePage + l + '/')
        # now add degrees
        if type(degree) == str:
            urls = [u+degree for u in urls]
        if type(degree) == list:
            urls = sum([[u+d for d in degree] for u in urls], [])
        if type(degree) == None:
            urls = sum([[u+d for d in CC.Degrees] for u in urls], [])

        # iterate over the 
        if college != None:
            print("college selection is not supported yet")
            exit()
        for url in urls:


        
        if "http://catalog.drexel.edu/coursedescriptions" not in self.driver.current_url:
            return {}
        courses = {}
        for elem in self.driver.find_elements_by_class_name("courseblock")[:5]:
            lines = elem.text.split("\n")
            title_line = lines[0].split(" ")
            course_number = " ".join(title_line[:2])
            courses[course_number] = {}
            courses[course_number]["name"] = " ".join(title_line[2:-2])
            courses[course_number]["credits"] = title_line[-2]
            courses[course_number]["description"] = lines[1]
            for line in lines[2:]:
                key = line.split(':')[0]
                val = line.replace(key+':', "").strip()
                courses[course_number][key] = val
        return courses
