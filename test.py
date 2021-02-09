
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import main
import TermMasterSchedule as TMS

#symbol_regex = r"\(([A-Z]{2,})\)"
#print(re.findall(symbol_regex, "Computer Science (CS)")[0])


t = main.Terms[0]
c = "Col of Computing & Informatics"
m = main.Colleges[c][0]

driver = webdriver.Chrome()
driver.get(TMS.HomePage)
elem = driver.find_element_by_link_text(t)
elem.click()
elem = driver.find_element_by_link_text(c)
elem.click()
elem = driver.find_element_by_link_text(m)
elem.click()

xpath_to_course_table = "/html/body/table/tbody/tr[2]/td/table[2]/tbody/tr[6]/td/table/tbody"
col_count = 9

rows = driver.find_elements_by_class_name("even") + driver.find_elements_by_class_name("odd")
rows = [elem.text for elem in rows]
print(rows[:5])




