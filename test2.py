import json
import Scraper

f = open('temp.txt', 'r')
header = f.readline()
current_section = []
count = 0
code = 'ANIM'
for line in f.readlines():
    if code in line and count > 3:
        print(''.join(current_section))
        input('...')
        count = 1
        current_section = [line]
    else:
        count += 1
        current_section.append(line)
f.close()