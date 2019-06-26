import sys
import re
i=0
def get_key_value (line):
    x = re.search (r'(\b\w+) .*\b\1( |$)', line)
    try:
        return x.group(1)
    except AttributeError:
        return None
with open('Passwords.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        x = get_key_value(line)
        if not x:
            i+=1
print(i)


