import re
def get_key_value (line):
    x = re.search (r'(\b\w+) .*\b\1( |$)', line)
    try:
        return x.group(1)
    except AttributeError:
        return None


z = 0
with open('Passwords.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        newline = re.sub(r'(\b\w+\b)',lambda m: ''.join(sorted(m.group(1))),line)
        if get_key_value(newline)==None:
            z+=1
print(z)
