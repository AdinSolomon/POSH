
from selenium import webdriver
import re
import json

HomePage = "http://catalog.drexel.edu/coursedescriptions/"

TermLengths = ["quarter", "semester"]
Degrees = ["undergrad", "grad"]
major_symbol_regex = r"\(([A-Z]{2,})\)"

def make_course_descriptions_url(term_length:str, student_status:str, major:str):
    major_symbol = re.findall(major_symbol_regex, major)[0]
    page = HomePage + \
           term_length + "/" + \
           student_status + "/" + \
           major_symbol.lower() + "/"
    return page

def scrape_course_descriptions(url:str):
    driver = webdriver.Chrome()
    driver.get(url)

    courses = {}
    for elem in driver.find_elements_by_class_name("courseblock")[:5]:
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
    
    driver.close()
    return courses