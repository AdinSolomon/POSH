
import TermMasterSchedule

Seasons = ["Fall", "Winter", "Spring", "Summer"]
Year = 21
TermLength = "Quarter" # or "Semester"
Terms = ["{0} {1} {2}-{3}".format(season, TermLength, Year-1, Year)   for season in Seasons] + \
        ["{0} {1} {2}-{3}".format(season, TermLength, Year-2, Year-1) for season in Seasons]
Colleges = ["Col of Computing & Informatics"]
Majors = ["Computer Science (CS)",
          "Software Engineering (SE)"]

termschedules = {}
for term in Terms:
    term_table = []
    print(term)
    for college in Colleges:
        print("\t"+college)
        for major in Majors:
            print("\t\t"+major)
            term_table.append(TermMasterSchedule.get_term_schedule(term, college, major))
    termschedules[term] = term_table

for row in termschedules[Terms[0]][:10]:
    print(row)









