
from selenium import webdriver

HomePage = "https://termmasterschedule.drexel.edu/webtms_du/app"
xpath_to_course_table = "/html/body/table/tbody/tr[2]/td/table[2]/tbody/tr[6]/td/table/tbody"

# Functions
def get_term_schedule(term:str, college:str, major:str) -> dict:
    # Eample return dictionary:
    # {
    #     "CS 150": {
    #         "Lab 862": {
    #             "style": "Remote Synchronous",
    #             "time": "F 01:00 pm - 02:50 pm",
    #             "professor": "Jeffrey L Popyack"
    #         },
    #         "Lecture A": {
    #             "style": "Remote Synchronous",
    #             "time": "M 04:00 pm - 05:50 pm\nDec 09, 2020 Final Exam:\n03:30 pm - 05:30 pm",
    #             "professor": "Jeffrey L Popyack"
    #         }
    #     }
    # }
    
    driver = webdriver.Chrome()
    try:
        driver.get(HomePage)
    except:
        print("Looks like the TMS has been moved!")
        return {}
    # Navigate to the term page
    try:
        elem = driver.find_element_by_link_text(term) # TODO - check for errors
        elem.click()
    except:
        print("Looks like that term's schedule isn't available yet!")
        return {}
    # Navigate to the college page
    try:
        elem = driver.find_element_by_link_text(college) # TODO - check for errors
        elem.click()
    except:
        print("Looks like there isn't any data for that college yet!")
        return {}
    # Navigate to the major's page
    try:
        elem = driver.find_element_by_link_text(major) # TODO - check for errors
        elem.click()
    except:
        print("Looks like there isn't any data for that major yet!")
        return{}

    # driver now holds the page with the term master schedule
    xpath_to_course_table = "/html/body/table/tbody/tr[2]/td/table[2]/tbody/tr[6]/td/table/tbody" # its also possible to just get the text from the whole table...
    total_rows = len(driver.find_elements_by_xpath(xpath_to_course_table + "/tr")) - 2 # for the header and footer
    col_count = 9 # just the td conut per row

    # fetch one row at a time
    #   - This is pretty slow, but fine for now
    #   - At some point just using regex on the text attribute of the course table is the move
    courses = {}
    
    for row_num in range(total_rows):
        row = [driver.find_element_by_xpath(xpath_to_course_table + "/tr[{0}]".format(2+row_num) + "/td[{0}]".format(c)).text for c in range(1, col_count+1)]
        course_number = " ".join(row[:2])
        if course_number not in courses:
            courses[course_number] = {}
        courses[course_number][f"{row[2]} {row[4]}"] = {
            "style": row[3],
            "time": row[7],
            "professor": row[8]
        }

    # Make sure to terminate the chrome instance!!!
    driver.close()

    # Return that dictionary
    return courses


