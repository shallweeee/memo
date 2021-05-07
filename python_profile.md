```python
def TEST():
    pass
    
if __name__ == '__main__':
    TEST()
```
```bash
time python -m cProfile test.py 2>&1 | tee prof.log

# or 

python -m cProfile -o program.prof test.py
snakeviz program.prof
```

