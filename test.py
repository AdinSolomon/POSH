
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

'''
driver = webdriver.Chrome()
driver.get(HomePage)
time.sleep(2)
elem = driver.find_element_by_link_text("Fall Quarter 20-21")
elem.click()
input("...\n")
elem.send_keys("FUCK")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
input("...\n")
driver.close()
'''

HomePage = "https://termmasterschedule.drexel.edu/webtms_du/app"
term = "Fall Quarter 20-21"
college = "Col of Computing & Informatics"
major = "Computer Science (CS)"

symbol_regex = "\(([A-Z]{2,})\)"
major_symbol = re.findall(symbol_regex, major)[0]

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
xpath_to_course_table = "/html/body/table/tbody/tr[2]/td/table[2]/tbody/tr[6]/td/table/tbody" # its also possible to just get the text from the whole table...
total_rows = len(driver.find_elements_by_xpath(xpath_to_course_table + "/tr")) - 2 # for the header and footer
col_count = 9 # just the td conut per row

print("{0} cells per row\n{1} total rows".format(col_count, total_rows))

'''
table = [[driver.find_element_by_xpath(xpath_to_course_table + "/tr[{0}]".format(2+n) + "/td[{0}]".format(c)).text for c in range(1, col_count+1)] for n in range(total_rows)]

input("Done generating table - print it?\n")
for row in table:
    print(row)
'''

info = driver.find_element_by_xpath(xpath_to_course_table).text
rows = [major_symbol+row for row in info.split(major_symbol)[1:]]







