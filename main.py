
import TermMasterSchedule
import json
import datetime

Seasons = ["Fall", "Winter", "Spring", "Summer"]
Year = 21
TermLength = "Quarter" # or "Semester"
Terms = ["{0} {1} {2}-{3}".format(season, TermLength, Year-1, Year)   for season in Seasons] #+ ["{0} {1} {2}-{3}".format(season, TermLength, Year-2, Year-1) for season in Seasons]
Colleges = {
    "Col of Computing & Informatics":
        ["Computer Science (CS)",
         "Software Engineering (SE)",
         "Computing and Informatics (CI)",
         "Data Science (DSCI)",
         "Information Science & Systems (INFO)"],
    "Arts and Sciences":
        ["Mathematics (MATH)"],
    "Antoinette Westphal COMAD":
        ["Game Art and Production (GMAP)"],
    "College of Engineering":
        ["ECE - Computers (ECEC)"]
}

if __name__ == "__main__":
    errlog = open("error_log.txt", "w")
    errlog.write("Time started: {0}\n".format(datetime.datetime.now()))

    course_offerings = {}
    for term in Terms[:1]:
        for college, majors in Colleges.items():
            for major in majors:
                print(f"{term}  -->  {college}  -->  {major}")
                if tms := TermMasterSchedule.get_term_schedule(term, college, major):
                    for course, sections_dict in tms.items():
                        if course not in course_offerings:
                            course_offerings[course] = {}
                        if term not in course_offerings[course]:
                            course_offerings[course][term] = {}
                        course_offerings[course][term] = sections_dict
                else:
                    errlog.write(f"{term}  -->  {college}  -->  {major}\n")
    
    errlog.write("Time ended: {0}\n".format(datetime.datetime.now()))
    errlog.close()

    f = open("Database\\TermMasterSchedule\\tms011.json", "w")
    f.write(json.dumps(course_offerings))
    f.close()









