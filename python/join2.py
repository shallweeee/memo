import pandas as pd

dic = {}
for f in 'abcd':
    with open(f, 'r') as fp:
        dic[f] = [l.strip() for l in fp.readlines()]

def mkdf(k, v):
    df = pd.DataFrame({k: v})
    t = '_' + k
    df[t] = df[k]
    df.index = df[t]
    df.index.name = None
    df[k] = 'O'
    return df.drop(t, axis=1)

dfs = [mkdf(k, v) for k, v in dic.items()]
df = pd.concat(dfs, axis=1)
df.fillna('')
df = df.sort_index()
df.to_csv('join2.csv')
