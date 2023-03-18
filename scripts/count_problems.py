import re
from collections import defaultdict

with open('fide.pgn', 'r') as f:
    data = f.read()

years = re.findall(r'FIDE Album (\d{4}-\d{4})', data)
count = defaultdict(int)

for year in years:
    count[year] += 1

sorted_count = sorted(count.items(), key=lambda x: int(x[0].split('-')[0]))

with open('output.txt', 'w') as f:
    for year, problems in sorted_count:
        f.write(f'FIDE Album {year} : {problems} problems  \n')