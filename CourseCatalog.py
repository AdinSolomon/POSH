
from selenium import webdriver
import re
import json

HomePage = "http://catalog.drexel.edu/coursedescriptions/"

TermLengths = ["quarter", "semester"]
Degrees = ["undergrad", "grad"]
major_symbol_regex = r"\(([A-Z-]{2,})\)"

def make_course_descriptions_url(term_length:str, student_status:str, major:str):
    major_symbol = re.findall(major_symbol_regex, major)[0]
    page = HomePage + \
           term_length + "/" + \
           student_status + "/" + \
           major_symbol.lower() + "/"
    return page
