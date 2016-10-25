from random import randint
import re

with open('moby_dick.txt') as fid:
   txt = fid.read()

txt = txt.lower()
txt = re.sub('[^a-z]', ' ', txt)
txt = re.sub('\s+', ' ', txt)

nlen = 6

ngramdict = {}

for i in range(nlen-1, len(txt)-1):
    t = txt[i-nlen+1:i+1]
    if t not in ngramdict:
        ngramdict[t] = {}
    sym = txt[i+1]
    if sym not in ngramdict[t]:
        ngramdict[t][sym] = 1
    else:
        ngramdict[t][sym] += 1

for key in ngramdict:
    symdict = ngramdict[key]
    tot = 0
    for sym in symdict:
        symdict[sym] += tot
        tot = symdict[sym]

string = next(key for key in ngramdict if key.startswith('the'))

for i in range(1000):
    symdict = ngramdict[string[-nlen:]]
    mx = max(symdict[key] for key in symdict)
    val = randint(1, mx)
    for key in symdict:
       if val <= symdict[key]:
           final_key = key
    string += final_key

print(string)
