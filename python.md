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
```
조사
```
help(df)
type(df)
id(df)
df is df1
```
