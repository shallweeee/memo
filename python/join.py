from functools import reduce
import pandas as pd

dic = {}
out = {}
for f in 'abcd':
    with open(f, 'r') as fp:
        dic[f] = [l.strip() for l in fp.readlines()]
    out[f] = []

while reduce(lambda s, v: s + len(v), dic.values(), 0) > 0:
    firsts = [v[0] for v in dic.values() if len(v) > 0]
    first = sorted(firsts)[0]
    for k, v in dic.items():
        word = (len(v) > 0 and v[0] == first) and first or ''
        out[k].append(word)

        if word:
            dic[k] = v[1:]

df = pd.DataFrame(out)
df.to_csv('join.csv', index=False)
