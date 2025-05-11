# mltiming

timing context manager for typical ML training

## Example usage

```python
from mltiming import timing

results = {}
with timing(dict=results, key="input") as t:
    # Simulate some processing 
    input()

print(t)
print(t.elapsed)
print(results)
```

## Example result

```
TimingResult(key='input', start=1049933.774409958, end=1049934.5090065)
0.734596542082727
{'input': 0.734596542082727}
```
