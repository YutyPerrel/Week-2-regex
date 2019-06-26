import sys
import re

def get_key_value (line):
    x = re.search(r'((^|.{2})([xo]).{2,3}\3.{2,3}\3(.{2}|$))|(^|.{3})([x]{3}|[o]{3})(.{3}|$)', line)
    if(x):
        if x.group(3)!=None:
            return(x.group(3))
        if x.group(6)!=None:
            return(x.group(6))
        #print(f"{line}= {x.groups()}")
    else:
        return(f'nothing')
while True:
    line = input("enter new action raw:")
    v = get_key_value(line)[0]
    if v != 'n':
        print(f'The winner is {v}')
        break
