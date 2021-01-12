시간
```
$ pip install six

>>> from datetime import datetime as dt
>>> from dateutil.relativedelta import relativedelta
>>> dt(2020, 12, 18) + relativedelta(days=90)
datetime.datetime(2021, 3, 18, 0, 0)
```
```
>>> dt.fromisoformat('2020-12-18')
datetime.datetime(2020, 12, 18, 0, 0)
```
생성
```
>>> [[3] * 3] * 3
[[3, 3, 3], [3, 3, 3], [3, 3, 3]]
>>> [1, 2, 3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
```
```
>>> list('abc')
['a', 'b', 'c']
```
```
>>> np.arange(9)
array([0, 1, 2, 3, 4, 5, 6, 7, 8])
>>> np.arange(9).reshape(3, 3)
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])
```
```
>>> pd.DataFrame([[1, 2, 3]])
   0  1  2
0  1  2  3
>>> pd.DataFrame([1, 2, 3])
   0
0  1
1  2
2  3
>>> pd.DataFrame({'A': {'a': 1, 'b': 3}, 'B': {'a': 2, 'b': 4}})
   A  B
a  1  2
b  3  4
>>> pd.DataFrame({'A': [1, 3], 'B': [2, 4]})
   A  B
0  1  2
1  3  4
```
```
>>> pd.DataFrame(np.random.randint(1, 10, (3, 3)), columns=list('abc'))
   a  b  c
0  3  4  6
1  7  2  7
2  6  6  1
>>> pd.DataFrame(np.random.randn(3,5))
          0         1         2         3         4
0  0.029041 -1.792245  1.471404  0.729562 -0.802141
1 -0.712027  0.295423 -0.273566  1.697214 -1.085588
2 -1.077688 -0.689995  0.775590 -0.232154 -1.255000
```
조사
```
df.info()
help(df)
type(df)
dir(df)
id(df)
df1 is df2
```
축
```
>>> df_dax = pd.DataFrame(np.arange(1,9).reshape(2,4))
>>> df = pd.DataFrame(np.arange(1,9).reshape(2,4))
>>> df.sum(axis=0)  # 축0 고정, 축1 을 따라 연산
0     6
1     8
2    10
3    12
dtype: int64
>>> df.sum(axis=1)  # 축1 고정, 축0 을 따라 연산
0    10
1    26
dtype: int64
```
csv
```
pd.read_csv(file_name_or_url, encoding='cp949')
pd.read_csv(file_name_or_url, engine='python')
pd.read_csv(file_name_or_url, usecols=['A', 'B'])  # A, B 컬럼만 로딩
```
예외
```
try:
    예외 발생 가능한 코드
except Exception as e:
    예외 발생시 실행
else:
    예외가 없을 때 실행
finally:
    항상 실행
```
인덱싱&슬라이싱
```
>>> df = pd.DataFrame(np.array([i+j for i in range(1, 6) for j in [10, 20, 30]]).reshape(5,3), columns=['c1', 'c2', 'c3'])
>>> df
   c1  c2  c3
0  11  21  31
1  12  22  32
2  13  23  33
3  14  24  34
4  15  25  35
>>> df[['c1', 'c2']][1:3]
   c1  c2
1  12  22
2  13  23
```
마스킹
```
>>> df[(df.c1 > 11) & (df.c3 < 34)]
   c1  c2  c3
1  12  22  32
2  13  23  33
```
팬시 검색
```
>>> df[['c1', 'c2']]
   c1  c2
0  11  21
1  12  22
2  13  23
3  14  24
4  15  25
>>> df.c2[[0,2,4]]
0    21
2    23
4    25
```
인덱서 검색
```
>>> df.lookup([0, 1], ['c1', 'c2'])
array([11, 22])
>>> df.iloc[0, 0]
11
>>> df.iloc[[0], 0]
0    11
Name: c1, dtype: int64
>>> type(df.iloc[[0], 0])
<class 'pandas.core.series.Series'>
>>> type(df.iloc[[0], [0]])
<class 'pandas.core.frame.DataFrame'>
```
사전 합치기
```
>>> d1 = {'a': 1}
>>> d2 = {'b': 2}
>>> {**d1, **d2}
{'a': 1, 'b': 2}
```
리스트 합치기
```
>>> l1 = [1]
>>> l2 = [2]
>>> l1 + l2
[1, 2]
```
