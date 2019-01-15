
# Python 3

### Deleting an element from a list
#### Deleting the n-th element in a list
```python
a = [1, 2, 3]
del a[1]
# a = [1, 3]

a = [1, 2, 3]
del a[1:]
# a = [1]
```

#### Deleting the first element found in list
```python
a = [1, 2, 3]
a.remove(2)
# a = [1, 3]
```

## Dictionaries

### Looping over dictionaries
#### Accessing keys
```python
for key in dic:
    print key
```
#### Accessing values
```python
for val in dic.values():
    print val
```
#### Accessing values
```python
for key, val in dic.items():
    print f"{key}, {val}"
```

## Strings

### Counting the occurrences of a character in a string
```python
s = "Quinnley"
n = s.count('n')
# n = 2
```

## Numbers

### Dividing two numbers and returning the floor
```python
f = 3 // 2
# f = 1
```

### Adding numbers in a list
```python
s = sum([1, 2, 3])
# s = 6
```

### Getting the highest number in a list
```python
m = max([1, 2, 3])
# m = 3
```

### Calculating the modulo between two numbers
```python
mod = 3 % 2
# mod = 1
```
