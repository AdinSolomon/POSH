
from selenium import webdriver
import re

HomePage = "https://termmasterschedule.drexel.edu/webtms_du/app"

# Functions
def get_term_schedule(term:str, college:str, major:str) -> list:
    driver = webdriver.Chrome()
    driver.get(HomePage)
    # Navigate to the term page
    elem = driver.find_element_by_link_text(term) # TODO - check for errors
    elem.click()
    # Navigate to the college page
    elem = driver.find_element_by_link_text(college) # TODO - check for errors
    elem.click()
    # Navigate to the major's page
    elem = driver.find_element_by_link_text(major) # TODO - check for errors
    elem.click()

    # driver now holds the page with the term master schedule
    xpath_to_course_table = "/html/body/table/tbody/tr[2]/td/table[2]/tbody/tr[6]/td/table/tbody" # its also possible to just get the text from the whole table...
    total_rows = len(driver.find_elements_by_xpath(xpath_to_course_table + "/tr")) - 2 # for the header and footer
    col_count = 9 # just the td conut per row

    # love me some one-liners
    table = [[driver.find_element_by_xpath(xpath_to_course_table + "/tr[{0}]".format(2+n) + "/td[{0}]".format(c)).text for c in range(1, col_count+1)] for n in range(total_rows)]

    return table
