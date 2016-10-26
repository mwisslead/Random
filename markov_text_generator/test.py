import random
import re

with open('moby_dick.txt') as fid:
   txt = fid.read()

worder = re.compile('(\w+\'?\w+)').findall

words = worder(txt.lower())
words = [word.replace('\'s', '') for word in words]

nlen = 6

ngramdict = {}

for i in range(nlen-1, len(words)-1):
    t = ' '.join(words[i-nlen+1:i+1])
    if t not in ngramdict:
        ngramdict[t] = {}
    sym = words[i+1]
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

string = worder(next(key for key in ngramdict))
for i in range(100):
    try:
        symdict = ngramdict[' '.join(string[-nlen:])]
        mx = max(symdict[key] for key in symdict)
        val = random.randint(1, mx)
        for key in symdict:
            if val <= symdict[key] <= mx:
                mx = symdict[key]
                final_key = key
        string += [final_key]
    except:
        string += worder(random.choice(list(ngramdict)))[0:1]

output = ['']
i = 0
while string:
    word = string.pop(0)
    if len(output[i]) + len(word) > 100:
        i += 1
        output.append('')
    output[i] += ' ' + word

print('\n'.join([l.strip() for l in output]))
