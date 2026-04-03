<div align="center">

# FuncBox

A lightweight Python utility library for common mathematical and algorithmic tasks.

</div>

<br/>

## Table of Contents

- [Install](#install)
- [Quick Start](#quick-start)
- [Functions Overview](#functions-overview)
- [API Reference](#api-reference)
- [Disclaimer](#disclaimer)
- [Contributing](#contributing)
- [License](#license)

## Install

### Latest Release:

```bash
pip install -U funcbox
```

or

```bash
python -m pip install -U funcbox
```

<!-- PYPI_FILTER_START -->

### Beta Version (Pre-release from GitHub):

```bash
pip install git+https://github.com/funcBox-i3/funcBox.git
```

or

```bash
python -m pip install git+https://github.com/funcBox-i3/funcBox.git
```

<!-- PYPI_FILTER_END -->

## Quick Start

```python
from funcbox import *

is_prime(17)
# True
classify_numbers([2, 3, 4, 5, 6])
# {'primes': [2, 3, 5], 'composites': [4, 6], 'neither': []}
fibonacci(10)
# 55
get_factors(12)
# [1, 2, 3, 4, 6]

d = Dig({"user": {"name": "Aditya Prasad S", "handle": "Pu94X", "age": 22}})
d("user.name")
# 'Aditya Prasad S'
d(["user.name", "user.handle", "user.age"])
# {'user.name': 'Aditya Prasad S', 'user.handle': 'Pu94X', 'user.age': 22}
```

## Functions Overview

> [!CAUTION]
> Functions marked **Beta** are under active development and their API - including parameter names, return types, and behaviour - may change at any time before a stable release. Do not rely on them in production without pinning to a specific version.

#### Algorithms

<!-- PYPI_FILTER_START -->

| Function                        | Description                                                     | Status    |
|---------------------------------|-----------------------------------------------------------------|-----------|
| [binary_search](#binary_search) | Searches for a value in a sorted sequence                       | Beta      |
| [dijkstra](#dijkstra)           | Calculates shortest paths in a graph using Dijkstra's algorithm | Published |

<!-- PYPI_FILTER_END -->
<!-- PYPI_UNCOMMENT_START
| Function | Description |
|----------|-------------|
| [binary_search](#binary_search) | Searches for a value in a sorted sequence |
| [dijkstra](#dijkstra) | Calculates shortest paths in a graph using Dijkstra's algorithm |
PYPI_UNCOMMENT_END -->

#### Number Theory

<!-- PYPI_FILTER_START -->

| Function                              | Description                                                     | Status    |
|---------------------------------------|-----------------------------------------------------------------|-----------|
| [classify_numbers](#classify_numbers) | Categorizes integers into prime, composite, and neutral subsets | Beta      |
| [fibonacci](#fibonacci)               | Computes the $n$-th Fibonacci term or sequence                  | Published |
| [get_factors](#get_factors)           | Computes all proper divisors of an integer                      | Published |
| [is_prime](#is_prime)                 | Determines whether a given integer is prime                     | Published |
| [primes](#primes)                     | Generates primes within a range via the Sieve of Eratosthenes   | Published |

<!-- PYPI_FILTER_END -->
<!-- PYPI_UNCOMMENT_START
| Function | Description |
|----------|-------------|
| [classify_numbers](#classify_numbers) | Categorizes integers into prime, composite, and neutral subsets |
| [fibonacci](#fibonacci) | Computes the $n$-th Fibonacci term or sequence |
| [get_factors](#get_factors) | Computes all proper divisors of an integer |
| [is_prime](#is_prime) | Determines whether a given integer is prime |
| [primes](#primes) | Generates primes within a range via the Sieve of Eratosthenes |
PYPI_UNCOMMENT_END -->

#### String Processing

<!-- PYPI_FILTER_START -->

| Function                | Description                                           | Status |
|-------------------------|-------------------------------------------------------|--------|
| [is_anagram](#isanagram) | Checks whether two strings are anagrams of each other | Beta  |

<!-- PYPI_FILTER_END -->
<!-- PYPI_UNCOMMENT_START
| Function | Description |
|----------|-------------|
| [is_anagram](#isanagram) | Checks whether two strings are anagrams of each other |
PYPI_UNCOMMENT_END -->

#### Data Utilities

<!-- PYPI_FILTER_START -->

| Function      | Description                                                         | Status |
|---------------|---------------------------------------------------------------------|--------|
| [dig](#dig)   | Wraps a nested dict for safe, repeated dot-path lookups             | Beta   |

<!-- PYPI_FILTER_END -->
<!-- PYPI_UNCOMMENT_START
| Function | Description |
|----------|-------------|
| [dig](#dig) | Wraps a nested dict for safe, repeated dot-path lookups |
PYPI_UNCOMMENT_END -->

## API Reference

### > `is_prime`

<a id="is_prime"></a>

```python
is_prime(n)
```

Determines whether a given integer is prime.

#### Usage

```python
is_prime(n: int) -> bool
```

**Parameters**

- `n` (int): The integer to evaluate. Must be a plain integer (not a `bool` or `float`).

**Raises**

- `TypeError`: Raised if `n` is not a plain integer.

**Returns**

- `bool`: `True` if the integer is prime, `False` otherwise.

**Examples**

```python
from funcbox import is_prime

print(is_prime(7))
# True
print(is_prime(10))
# False
```

---

### > `classify_numbers`

<a id="classify_numbers"></a>

```python
classify_numbers(numbers)
```

Categorizes a sequence of integers into prime, composite, and neutral sets (0, 1, or negative numbers).

#### Usage

```python
classify_numbers(numbers: list[int]) -> dict[str, list[int]]
```

**Parameters**

- `numbers` (list[int]): A list of integers to categorize. All elements must be plain integers.

**Raises**

- `TypeError`: Raised if `numbers` is not a list, or if any element is not a plain integer.

**Returns**

- `dict`: A dictionary containing three lists:
    - `'primes'`: Integers that are prime.
    - `'composites'`: Integers that are composite (greater than 1 and not prime).
    - `'neither'`: Integers that are neither prime nor composite (< 2).

**Examples**

```python
from funcbox import classify_numbers

print(classify_numbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
# {'primes': [2, 3, 5, 7], 'composites': [4, 6, 8, 9], 'neither': [0, 1]}
print(classify_numbers([-5, 0, 1, 13, 15]))
# {'primes': [13], 'composites': [15], 'neither': [-5, 0, 1]}
```

---

### > `fibonacci`

<a id="fibonacci"></a>

```python
fibonacci(n, output_type="int")
```

Computes Fibonacci sequence values. Supports retrieving an individual $n$-th term or an array containing the sequence up
to the $n$-th element.

#### Usage

```python
fibonacci(n: int, output_type: str = "int") -> int | list[int]
```

**Parameters**

- `n` (int): The sequence index (0-indexed) or the total count of elements to generate. Must be a plain integer.
- `output_type` (str): Specification for the return format.
    - `"int"` (default): Returns a single integer corresponding to the $n$-th term.
    - `"list"`: Returns a list consisting of the first `n` terms.

**Returns**

- `int` if `output_type` is `"int"`.
- `list[int]` if `output_type` is `"list"`.

**Raises**

- `TypeError`: Raised if `n` is not a plain integer or `output_type` is not a string.
- `ValueError`: Raised if `n` is a negative integer or if an unsupported `output_type` is provided.

**Examples**

```python
from funcbox import fibonacci

print(fibonacci(0))
# 0
print(fibonacci(5))
# 5
print(fibonacci(5, output_type="list"))
# [0, 1, 1, 2, 3]
```

---

### > `get_factors`

<a id="get_factors"></a>

```python
get_factors(num)
```

Computes all proper divisors (factors) of an integer, excluding the number itself.

#### Usage

```python
get_factors(num: int) -> list[int]
```

**Parameters**

- `num` (int): The target integer to compute factors for. Must be a plain integer (not a `bool` or `float`).

**Raises**

- `TypeError`: Raised if `num` is not a plain integer.

**Returns**

- `list[int]`: A sorted list of all proper factors.

**Examples**

```python
from funcbox import get_factors

print(get_factors(12))  # [1, 2, 3, 4, 6]
print(get_factors(7))   # [1]
```

---

### > `dig`

<a id="dig"></a>

```python
dig(data)
```

Wraps a nested dictionary once and lets you query it repeatedly using dot-path strings, explicit key sequences, or multi-path batches - all through a single, consistent interface.

#### Usage

```python
dig(data: dict[str, Any])
```

**Parameters**

- `data` (dict[str, Any]): The source dictionary to wrap.

**Raises**

- `TypeError`: Raised if `data` is not a `dict`.

**Path types**

The type of `path` passed to any lookup determines behaviour:

| Type | Behaviour |
|---|---|
| `str` | Dot-separated path such as `"user.address.city"`. Numeric segments like `"0"` are automatically treated as list indices when traversing sequences. |
| `tuple` | Explicit key/index sequence such as `("user", 0, "name")`. Use when keys contain dots or you need unambiguous integer indices. |
| `list` | **Multi-path batch** - each item is its own `str` or `tuple` path. Returns a `dict` mapping every path string to its resolved value. `default` and `last` apply uniformly. |

**Methods**

| Syntax | Description |
|---|---|
| `d(path)` | Resolve a path - returns the value or `None` on failure |
| `d(path, default=…)` | Same, with an explicit fallback value |
| `d(path, last=True)` | Returns the deepest resolved value instead of `default` on failure |
| `d([path1, path2, …])` | Resolve multiple paths in one call - returns a `dict` |
| `d[path]` | Subscript shorthand for `d(path)` |
| `path in d` | `True` if the path resolves to an existing key (even if the value is `None`) |
| `d.scope(path)` | Returns a new `dig` rooted at the sub-dict at `path` |

**Raises** (on lookup)

- `TypeError`: If `path` is not a `str`, `tuple`, or `list`; or if a multi-path list entry is not a `str` or `tuple`.
- `KeyError`: If `path` passed to `scope()` does not exist.
- `TypeError`: If the value at `path` passed to `scope()` is not a `dict`.

**Returns**

- `Any` - the resolved value for single-path lookups.
- `dict[str, Any]` - a mapping of each path to its result for multi-path lookups.
- `dig` - a new scoped instance when calling `scope()`.

**Examples**

```python
from funcbox import Dig

data = {
  "user": {
    "name": "Aditya Prasad S",
    "handle": "Pu94X",
    "age": 19,
    "email": None,
    "address": {
      "city": "Chennai",
      "state": "Tamil Nadu",
      "zip": "600001",
    },
    "projects": [
      {"name": "funcBox", "stars": 42, "lang": "Python"},
      {"name": "InfiniKit", "stars": 18, "lang": "Kotlin"},
    ],
    "settings": {
      "theme": "dark",
      "notifications": {"email": True, "push": False},
    },
  }
}

d = Dig(data)

# single dot-path
d("user.name")  # 'Aditya Prasad S'
d("user.handle")  # 'Pu94X'
d("user.address.city")  # 'Chennai'

# missing key → default
d("user.phone", default="N/A")  # 'N/A'

# last=True → deepest resolved value before the miss
d("user.phone", last=True)  # {'city': 'Chennai', 'state': 'Tamil Nadu', 'zip': '600001'}

# numeric segment traverses a list
d("user.projects.0.name")  # 'funcBox'
d("user.projects.1.lang")  # 'Kotlin'

# tuple path - explicit key sequence (useful when keys contain dots)
d(("user", "projects", 0, "stars"))  # 42

# subscript shorthand
d["user.age"]  # 19
d["user.settings.theme"]  # 'dark'

# membership test - True even when the value is None
"user.email" in d  # True  (key exists, value is None)
"user.phone" in d  # False (key doesn't exist)

# multi-path: resolve several values in one call
d(["user.name", "user.handle", "user.age"])
# {'user.name': 'Aditya Prasad S', 'user.handle': 'Pu94X', 'user.age': 19}

d(["user.projects.0.name", "user.projects.1.name"], default="unknown")
# {'user.projects.0.name': 'funcBox', 'user.projects.1.name': 'InfiniKit'}

# scope: zoom into a sub-node - avoids repeating the prefix
addr = d.scope("user.address")
addr("city")  # 'Chennai'
addr["zip"]  # '600001'
addr(["city", "state", "zip"])  # {'city': 'Chennai', 'state': 'Tamil Nadu', 'zip': '600001'}

# scope into a list element
proj = d.scope("user.projects.0")
proj("name")  # 'funcBox'
proj("stars")  # 42

# nested scope
notif = d.scope("user.settings.notifications")
notif("email")  # True
notif("push")  # False

# repr
repr(d)  # Dig({'user'})
repr(addr)  # Dig({'city', 'state', 'zip'})
```

> **Note:** Numeric string segments like `"0"` in a dot-path are automatically coerced to integer indices when the current node is a `list` or `tuple`. Use a `tuple` path with an `int` element (e.g. `("user", "projects", 0, "name")`) for unambiguous index access.

---

### > `is_anagram`

<a id="isanagram"></a>

```python
is_anagram(str1, str2, case=False, spaces=False, punct=False)
```

Checks if two strings are anagrams of each other.

#### Usage

```python
is_anagram(str1: str, str2: str, case: bool = False, spaces: bool = False, punct: bool = False) -> bool
```

**Parameters**

- `str1` (str): First string to compare.
- `str2` (str): Second string to compare.
- `case` (bool): Ignore case when comparing. Defaults to `False`.
- `spaces` (bool): Ignore spaces when comparing. Defaults to `False`.
- `punct` (bool): Ignore punctuation when comparing. Defaults to `False`.

**Raises**

- `TypeError`: Raised if `str1` or `str2` is not a string.

**Returns**

- `bool`: `True` if the strings are anagrams, `False` otherwise.

**Examples**

```python
from funcbox import is_anagram

print(is_anagram("listen", "silent"))
# True
print(is_anagram("Listen", "Silent", case=True))
# True
print(is_anagram("a gentleman", "elegant man", spaces=True))
# True
print(is_anagram("Astronomer!", "Moon starer", case=True, punct=True, spaces=True))
# True
print(is_anagram("hello", "world"))
# False
```

---

### > `binary_search`

<a id="binary_search"></a>

```python
binary_search(arr, target)
```

Searches for a target value in a sorted sequence.

#### Usage

```python
binary_search(arr: Sequence, target: Any) -> int
```

**Parameters**

- `arr` (Sequence): A sorted sequence to search through (e.g. `list`, `tuple`, `range`).
- `target` (Any): The value to search for.

**Returns**

- `int`: The index of the target if found, `-1` otherwise.

**Raises**

- `TypeError`: Raised if `arr` is not a `Sequence`.

**Examples**

```python
from funcbox import binary_search

print(binary_search([1, 3, 5, 7, 9], 7))
# 3
print(binary_search([1, 3, 5, 7, 9], 4))
# -1
```

---

### > `dijkstra`

<a id="dijkstra"></a>

```python
dijkstra(graph, start_node, end_node=None)
```

Calculates the shortest paths from a source node to all other reachable nodes in a weighted graph using Dijkstra's
algorithm.

#### Usage

```python
dijkstra(graph: dict, start_node: Any, end_node: Any = None) -> dict
```

**Parameters**

- `graph` (dict): An adjacency list where each node maps to a `dict` of `{neighbor: weight}` pairs. All weights must be
  non-negative numbers and all neighbor keys must be nodes in the graph.
- `start_node`: The origin node for pathfinding computation.
- `end_node`: Optional terminal node. If provided, the algorithm terminates early once the shortest path to this node is
  found.

**Raises**

- `ValueError`: Raised if `graph` is not a `dict`, any node's adjacency value is not a `dict`, any neighbor key is not
  present in the graph, any edge weight is not a number or is negative, `start_node` is not in the graph, or `end_node`
  is specified but not in the graph.

**Returns**

- `dict`: A resultant dictionary comprised of two objects:
    - `'distances'`: The calculated minimum distances from the `start_node` to all resolved nodes. Unreachable nodes
      evaluate to positive infinity (`float('inf')`).
    - `'paths'`: Ordered sequences of nodes representing the shortest path from the `start_node`. Unreachable nodes map
      to `None`.

**Examples**

```python
from funcbox import dijkstra
from pprint import pprint

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5, 'E': 1},
    'C': {'B': 1, 'E': 3},
    'D': {'F': 2},
    'E': {'D': 1, 'F': 4},
    'F': {}
}

result = dijkstra(graph, 'A')

pprint(result['distances']) 
# {'A': 0, 'B': 3, 'C': 2, 'D': 5, 'E': 4, 'F': 7}
pprint(result['paths'])
# {'A': ['A'],
#  'B': ['A', 'C', 'B'],
#  'C': ['A', 'C'],
#  'D': ['A', 'C', 'B', 'E', 'D'],
#  'E': ['A', 'C', 'B', 'E'],
#  'F': ['A', 'C', 'B', 'E', 'D', 'F']}

result = dijkstra(graph, 'A', 'F')
print(result['distances']['F']) 
# 7
print(result['paths']['F'])
#  ['A', 'C', 'B', 'E', 'D', 'F']
```

---

### > `primes`

<a id="primes"></a>

```python
primes(start, limit)
```

Generates a sequence of prime numbers within a specified bounds utilizing the Sieve of Eratosthenes algorithm.

#### Usage

```python
primes(start: int = 2, limit: int) -> list[int]
```

**Parameters**

- `start` (int): The inclusive lower bound for prime generation. Defaults to 2.
- `limit` (int): The inclusive upper bound for prime generation.

**Returns**

- `list[int]`: An ordered list of prime numbers from `start` boundary up to the specified `limit`.

**Raises**

- `TypeError`: Raised if `start` or `limit` is not a plain integer.
- `ValueError`: Raised if either `limit` or `start` are evaluated to be less than 2.

**Examples**

```python
from funcbox import primes

print(primes(limit=10))
# [2, 3, 5, 7]
print(primes(start=10, limit=20))
# [11, 13, 17, 19]
```

## Disclaimer

FuncBox provides utility functions for general use. The developer is not responsible for any issues caused by improper
use or abuse of the library.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.