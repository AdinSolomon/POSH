
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
#rows_elems = driver.find_elements_by_class_name("even") + driver.find_elements_by_class_name("odd")

#course_table = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table[2]/tbody/tr[6]/td/table")
#first_row = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table[2]/tbody/tr[6]/td/table/tbody/tr[@class='even']/td")







