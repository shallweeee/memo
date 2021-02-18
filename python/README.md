```bash
for f in a b c d; do
  while read t; do grep -qw $t source_$f && echo $t; done < tok > $f
done
python join.py
python join2.py
```
