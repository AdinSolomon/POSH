
import requests
import lxml
from bs4 import BeautifulSoup
import datetime

HomePage = "https://termmasterschedule.drexel.edu/webtms_du/app"
TodaysDate = datetime.date.today()

Seasons = ["Fall", "Winter", "Spring", "Summer"]
Year = 21
TermLength = "Quarter" # or "Semester"
Links = ["{0} {1} {2}-{3}".format(season, TermLength, Year-1, Year) for season in Seasons] + ["{0} {1} {2}-{3}".format(season, TermLength, Year-2, Year-1) for season in Seasons]

College = "Col of Computing & Informatics"
Majors = ["Computer Science (CS)",
          "Software Engineering (SE)"]

# Get rows by whether the elements are of class "even" or "odd" (table has alternating colors)

# Just compile a list of course numbers and titles I guess

# Functions
def get_term_schedule(term:str = "Fall Quarter 20-21", college:str = "Col of Computing & Informatics", major:str = "Computer Science (CS)") -> list:
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
    # The information is in a table with alternating row colors
    rows_elems = driver.find_elements_by_class_name("even") + driver.find_elements_by_class_name("odd")

