
# Python 3

## Lists

### Removing and returning an element from the start of a list
```python
a = [1, 2, 3, 4, 5]
a.pop(0)
# 1
# a = [2, 3, 4, 5]
```

#### For large queues, use deque
```python
from collections import deque

a = deque([1, 2, 3, 4, 5])
a.popleft()
# 1
# a = [2, 3, 4, 5]
```

### Getting common elements in two lists
```python
a1 = [1, 2, 3, 4, 5]
a2 = [3, 4, 5, 6, 7]

# convert to sets and calculate intersection
b = list(set(a1) & set(a2))
# b = [3, 4, 5]
```

### Filtering a list comprehension with an if statement
```python
groups = {
    'a': [1, 2, 3],
    'b': [4, 5],
    'c': [6]
}

# keep groups with 2 or more elements
g = [group for group in groups if len(group) >= 2]
# g = [[1, 2, 3], [4, 5]]
```

### Merging two lists
```python
a1 = [1, 2, 3]
a2 = [4, 5, 6]

# old school
m = a1 + a2
# m = [1, 2, 3, 4, 5, 6]

# >= python 3.5
m = [*a1, *a2]
# m = [1, 2, 3, 4, 5, 6]
```

### Setting a starting index value for enumerate
```python
a = [1, 2, 3]

for idx, val in enumerate(a, start=1)
    print f"{idx}: {val}"
# 1: 1
# 2: 2
# 3: 3
```

### Getting the last element of a list
```python
a = [1, 2, 3]
a[-1]
# a = 3
```

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


## Dictionaries and Sets

### Using sets
```python
# sets are implemented as a value-less hash table
# unordered and no duplicate elements
# great for membership testing and eliminating duplicates
# create an empty set
s = set()

# add an element
s.add('a')

# remove an element, raises a KeyError if element doesn't exist
s.remove('a')

# remove an element
s.discard('a')

a = {1, 2, 3}
b = {3, 4, 5}

# a is a subset of b
a <= b
# False

# elements in a that are not in b
a - b
# {1, 2}

```

### Removing the last inserted element from an ordered dict
```python
from collections import OrderedDict

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d.popitem(last=False)
# 1
```

### Removing and returning an element from a dict
```python
d = {'a': 1, 'b': 2, 'c': 3}
d.pop('b')
# 2

# set default value if key not found
d.pop('b', None)
# None
```

### Subtracting counters
```python
from collections import Counter

c = Counter(a=3, b=1)
d = Counter(a=1, b=2)

# subtract and keep only positive counts
c - d
# {'a': 2}
```

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
#### Accessing key, values
```python
for key, val in dic.items():
    print f"{key}, {val}"
```


## Strings

### Formatting strings containing expressions
```python
name = "Rick"
f"He said his name is {name}."
# 'He said his name is Rick.'

today = datetime(year=2019, month=2, day=14)
f"{today:%B %d, %Y}"
# 'February 14, 2019'
```

### Converting a string to lowercase
```python
s = "Quinnley"
s.lower()
# quinnley
```

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

## Dates and times

### Getting the current unix timestamp
```python
import time

time.time()
```


## Iterators and Generators

### Getting the first element that matches a condition
```python
a = [1, 2, 3, 4, 5]

# get first element > 3
next((x for x in a if x > 3), None)
```


## Classes and Objects

### Defining a hashable collection
```python
# define the __hash__ and __eq__ special methods
def __hash__(self):
    return hash(frozenset(self.values))

def __eq__(self, other):
    return set(self.values) == set(other.values)
```


## Regular Expressions

### Searching strings and extracting groups
```python
import re

s = "abc123"

match = re.search(r"^([a-zA-Z]+)(\d+)$", s)

if match:
    groups = match.groups()

# groups = ("abc", "123")
```