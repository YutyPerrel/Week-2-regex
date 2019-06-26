import sys
import re

def get_key_value (line):
    x = re.search(r'^([x]{3}|[o]{3}).{6}$|^.{3}([x]{3}|[o]{3}).{3}$|^.{6}([x]{3}|[o]{3})$|^..([xo]).\4.\4..$|^([xo])...\5...\5$|^..([xo])..\6..\6|^([ox])..\7..\7..$', line)
    if(x):
        if x.group(1)!=None:
            return(x.group(1))
        if x.group(2)!=None:
            return(x.group(2))
        if x.group(3)!=None:
            return(x.group(3))
        if x.group(4)!=None:
            return(x.group(4))
        if x.group(5)!=None:
            return(x.group(5))
        if x.group(6)!=None:
            return(x.group(6))
        if x.group(7)!=None:
            return(x.group(7))
        #print(f"{line}= {x.groups()}")
    else:
        return(f'nothing')

    """
    x = re.search (r'^([x]{3}|[o]{3}).{6}$', line)
    if x:
        print(f"x[1]= {x[1]}")
    y = re.search(r'^.{3}([x]{3}|[o]{3}).{3}$', line)
    if y:
        print(f"y[1]= {y.group(1)}")
    z = re.search(r'^.{6}([x]{3}|[o]{3})$', line)
    if z:
        print(f"z[1]= {z.group(1)}")
    a = re.search(r'^..([xo]).\1.\1..$', line)
    if a:
        print(f"a[1]= {a.group(1)}")
    b = re.search(r'^([xo])...\1...\1$', line)
    if b:
        print(f"b[1]= {b.group(1)}")
        """

while True:
    line = input("enter new action raw:")

#with open('xo.txt', 'r', encoding='UTF-8') as f:
    #for line in f:
    v = get_key_value(line)[0]
    if v != 'n':
        print(f'The winner is {v}')
        break
