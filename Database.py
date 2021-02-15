
import os
import json
from selenium import webdriver

import util
import CourseCatalog as CC
import TermMasterSchedule as TMS

SEP = "\\"
ALL_SUBJECTS = []
datetime_format = "%Y-%m-%d %H:%M:%S"

class NotASubjectFile(Exception):
    pass

def init():
    os.makedirs("Database", exist_ok=True)

def get_subject(subject_symbol:str) -> dict:
    json_filepath = "{0}{1}{2}.json".format("Database", SEP, subject_symbol)
    try:
        json_file = open((json_filepath, 'r'))
        data = json.load(json_file)
        json_file.close()
        return data
    except json.decoder.JSONDecodeError:
        raise NotASubjectFile
    except FileNotFoundError:
        return {}
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





if __name__ == "__main__":
    print(__file__)