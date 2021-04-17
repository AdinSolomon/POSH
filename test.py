
import json
import re

P_KEY = "Prerequisites"
Ps = []
f = open(r'Database\Subjects\CS.json')
for v in json.load(f)["Courses"].values():
    if P_KEY not in v:
        continue
    prereq = v[P_KEY]
    prereq = prereq.replace("(Can be taken Concurrently)", "CBTC")
    if ',' in prereq:
        print(prereq)
    Ps.append(prereq)
f.close()

#print('\n'.join(Ps))

