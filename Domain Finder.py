import re
with open('Downloads/domains.txt', 'r') as f:
    for line in f:
        if '.k12.' in line:
            domain = re.search('@[\w.]+', line)
            print domain.group()
        else:
            pass


