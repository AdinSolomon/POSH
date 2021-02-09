
import os
import json
from selenium import webdriver, WebDriver
import CourseCatalog as CC
import TermMasterSchedule as TMS

SEP = "\\"
ALL_SUBJECTS = ["ALL_SUBJECTS"]

def path_cat(a:str, b:str) -> str:
    return a + (SEP if a[-1])

def init():
    os.makedirs("Database", exist_ok=True)

    # Get a comprehensive list of the 
    #driver = webdriver.Chrome()
    #for term in Terms:
    #    driver.get(TMS.HomePage)
    #    driver.find_element_by_link_text(term).click()
    #    colleges = [elem.text for elem in driver.find_elements_by_xpath("/html/body/table/tbody/tr[2]/td/table[2]/tbody/tr[4]/td/div/a")]
    #    for college in colleges:
    #        driver.find_element_by_link_text(college).click()
    #        for subject in driver.find_elements_by_class_name("even") + driver.find_elements_by_class_name("odd"):
    #            subject_symbol = re.findall(symbol_regex, subject.text)[-1]
    #            os.makedirs(SEP.join(["Database", subject_symbol]), exist_ok=True)
    #driver.close()
    
    # Create a different JSON for each subject

def get_subject(subject_symbol:str) -> dict:
    json_filepath = "{0}{1}{2}.json".format("Database", SEP, subject_symbol)
    json_file = open((json_filepath, 'r'))
    data = json.load(json_file)
    json_file.close()
    return data
def update_subject(subject_symbol:str, new_data) -> None:
    json_filepath = "{0}{1}{2}.json".format("Database", SEP, subject_symbol)
    json_file = None
    data = {}
    try:
        json_file = open(json_filepath, 'x')
    except FileExistsError:
        json_file = open(json_filepath, 'r+')
        old_data = json.load(json_file)
    data.update(new_data)
    json.dump(data, json_file)
    