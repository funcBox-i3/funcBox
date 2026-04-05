<div align="center">

# FuncBox

A lightweight Python utility library for common mathematical and algorithmic tasks.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?logo=opensourceinitiative&logoColor=white)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![PyPI Version](https://img.shields.io/pypi/v/funcbox.svg?logo=pypi&logoColor=white)](https://pypi.org/project/funcbox/)
[![GitHub](https://img.shields.io/badge/GitHub-funcBox-181717.svg?logo=github&logoColor=white)](https://github.com/funcBox-i3/funcBox)

</div>

<br/>

## Table of Contents

- [Install](#install)
- [Quick Start](#quick-start)
- [Functions Overview](#functions-overview)
- [API Reference](#api-reference)
- [Disclaimer](#disclaimer)
- [Contributing](#contributing)
- [Issues & Bug Reports](#issues--bug-reports)
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

### Requirements

- **Python 3.8+** - FuncBox is compatible with Python 3.8 and newer versions.
- **No external dependencies** - FuncBox is a lightweight library with zero external dependencies, using only Python's standard library.

## Quick Start

```python
from funcbox import *

is_prime(17)
# True

classify_numbers([2, 3, 4, 5, 6])
# {'primes': [2, 3, 5], 'composites': [4, 6], 'neither': []}

d = Dig({"user": {"name": "Aditya Prasad S", "handle": "Pu94X", "age": 22}})
d("user.name")
# 'Aditya Prasad S'
d(["user.name", "user.handle", "user.age"])
# ['Aditya Prasad S', 'Pu94X', 22]
```

## Functions Overview

> [!IMPORTANT]
> Functions marked **Beta** are under active development and their API - including parameter names, return types, and behaviour - may change at any time before a stable release. Do not rely on them in production. For stable, published versions of the library, see the [PyPI project page](https://pypi.org/project/funcbox/).

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

| Function                                    | Description                                                    | Status |
|---------------------------------------------|----------------------------------------------------------------|--------|
| [fuzzy_search](#fuzzy_search)               | Ranks candidates by fuzzy similarity to a query string         | Beta   |
| [is_anagram](#isanagram)                    | Checks whether two strings are anagrams of each other          | Beta   |
| [is_null_or_blank](#is_null_or_blank)       | Returns `True` if a value is `None`, a whitespace-only string, or an empty collection | Beta   |
| [levenshtein_distance](#levenshtein_distance) | Returns the Levenshtein edit distance between two strings    | Beta   |
| [similarity](#similarity)                   | Scores the fuzzy similarity between two strings                | Beta   |
| [truncate](#truncate)                       | Shortens a string to a maximum length, appending a suffix      | Beta   |

<!-- PYPI_FILTER_END -->
<!-- PYPI_UNCOMMENT_START
| Function | Description |
|----------|-------------|
| [fuzzy_search](#fuzzy_search) | Ranks candidates by fuzzy similarity to a query string |
| [is_anagram](#isanagram) | Checks whether two strings are anagrams of each other |
| [is_null_or_blank](#is_null_or_blank) | Returns `True` if a value is `None`, a whitespace-only string, or an empty collection |
| [levenshtein_distance](#levenshtein_distance) | Returns the Levenshtein edit distance between two strings |
| [similarity](#similarity) | Scores the fuzzy similarity between two strings |
| [truncate](#truncate) | Shortens a string to a maximum length, appending a suffix |
PYPI_UNCOMMENT_END -->

#### Data Utilities

<!-- PYPI_FILTER_START -->

| Function      | Description                                                         | Status |
|---------------|---------------------------------------------------------------------|--------|
| [dig](#dig)   | Wraps a nested object (dict, list, or tuple) for safe, repeated dot-path lookups | Beta   |

<!-- PYPI_FILTER_END -->
<!-- PYPI_UNCOMMENT_START
| Function | Description |
|----------|-------------|
| [dig](#dig) | Wraps a nested dict for safe, repeated dot-path lookups |
PYPI_UNCOMMENT_END -->

## API Reference

> [!TIP]
> Functions are organized by category below. Each function includes its signature, parameters, return type, and practical examples.

### Algorithms

---

### `binary_search(arr, target)`

<a id="binary_search"></a>

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

### `dijkstra(graph, start_node, end_node=None)`

<a id="dijkstra"></a>

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

### Number Theory

---

### `classify_numbers(numbers)`

<a id="classify_numbers"></a>

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

### `fibonacci(n, output_type="int")`

<a id="fibonacci"></a>

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

### `get_factors(num)`

<a id="get_factors"></a>

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

### `is_prime(n)`

<a id="is_prime"></a>

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

### `primes(start, limit)`

<a id="primes"></a>

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

---

### String Processing

---

### `fuzzy_search(query, candidates, *, threshold=0.0, limit=None, key=None)`

<a id="fuzzy_search"></a>

Finds the best fuzzy matches for *query* within *candidates*, scoring each item by a blend of three signals: OSA edit-distance similarity (weight 0.5), ordered subsequence coverage (weight 0.3), and partial-window ratio (weight 0.2). Results are sorted best-first. This function has **zero external dependencies**.

#### Usage

```python
fuzzy_search(
    query: str,
    candidates: Sequence[Any],
    *,
    threshold: float = 0.0,
    limit: int | None = None,
    key: Callable | None = None,
) -> list[dict[str, Any]]
```

**Parameters**

- `query` (str): The search string.
- `candidates` (Sequence): Items to search through. Must be strings, or use *key* for arbitrary objects.
- `threshold` (float): Minimum score (inclusive) in `[0.0, 1.0]`. Candidates scoring below this are excluded. Defaults to `0.0`.
- `limit` (int | None): Maximum number of results to return. `None` returns all matches above the threshold.
- `key` (callable | None): Extracts the comparison string from each candidate. When `None`, candidates must be strings.

**Returns**

- `list[dict]`: A list of dicts sorted by `'score'` descending, each containing:
    - `'match'` – the original candidate item.
    - `'score'` – similarity score as a `float` in `[0.0, 1.0]`.

**Raises**

- `TypeError`: If `query` is not a `str`, `candidates` is not a `Sequence` (or is a bare `str`), `key` is not callable (when provided), or any candidate is not a `str` when no *key* is given.
- `ValueError`: If `threshold` is outside `[0.0, 1.0]`, or `limit` is not a positive integer.

**Examples**

```python
from funcbox import fuzzy_search

# Basic string search
fuzzy_search("pyth", ["Python", "Ruby", "Rust", "PyPy"])
# [{'match': 'Python', 'score': 0.8333}, {'match': 'PyPy', 'score': 0.75}, ...]

# Tolerate typos
fuzzy_search("dijktra", ["dijkstra", "binary search", "bubble sort"])
# [{'match': 'dijkstra', 'score': 0.8804}, ...]

# Filter by minimum score
fuzzy_search("rust", ["Python", "Ruby", "Rust"], threshold=0.5)
# [{'match': 'Rust', 'score': 1.0}]

# Limit results
fuzzy_search("py", ["Python", "PyPy", "Ruby", "Rust"], limit=2)
# [{'match': 'PyPy', 'score': ...}, {'match': 'Python', 'score': ...}]

# Search objects with a key function
people = [{"name": "Alice"}, {"name": "Alicia"}, {"name": "Bob"}]
fuzzy_search("alic", people, key=lambda p: p["name"])
# [{'match': {'name': 'Alice'}, 'score': ...}, {'match': {'name': 'Alicia'}, 'score': ...}]

# Score meaning: 1.0 = exact match, 0.0 = completely dissimilar
fuzzy_search("hello", ["hello", "helo", "world"])
# [{'match': 'hello', 'score': 1.0}, {'match': 'helo', 'score': 0.85}, {'match': 'world', 'score': 0.1}]
```

---

### `similarity(query, candidate)`

<a id="similarity"></a>

Scores the fuzzy similarity between two strings using a blend of three signals: OSA edit-distance ratio (weight 0.5), ordered subsequence coverage (weight 0.3), and partial-window ratio (weight 0.2). OSA distance correctly treats transpositions of adjacent characters as a single edit, improving accuracy over plain Levenshtein for common typos. This is the same scoring function used internally by [`fuzzy_search`](#fuzzy_search), exposed for cases where you want to score a single pair directly.

#### Usage

```python
similarity(query: str, candidate: str) -> float
```

**Parameters**

- `query` (str): The reference string (e.g. the user's search term).
- `candidate` (str): The string to score against *query*.

**Returns**

- `float`: A score in `[0.0, 1.0]`. `1.0` means identical (case-insensitively); `0.0` means completely dissimilar.

**Raises**

- `TypeError`: If either argument is not a `str`.

**Examples**

```python
from funcbox import similarity

print(similarity("hello", "hello"))
# 1.0

print(similarity("pyth", "Python"))   # partial prefix
# 0.8333

print(similarity("dijktra", "dijkstra"))  # typo tolerance
# 0.8804

print(similarity("pytohn", "python"))  # transposition — 1 edit (OSA)
# 0.7833

print(similarity("search", "fuzzy_search"))  # substring in longer string
# 0.75

print(similarity("abc", "xyz"))  # no overlap
# 0.0

# Sort a list manually by score
words = ["Python", "PyPy", "Ruby", "Rust"]
words.sort(key=lambda w: similarity("pyth", w), reverse=True)
print(words)
# ['Python', 'PyPy', 'Rust', 'Ruby']
```

---

### `levenshtein_distance(a, b)`

<a id="levenshtein_distance"></a>

Returns the Levenshtein edit distance between two strings — i.e., the minimum number of single-character **insertions**, **deletions**, and **substitutions** required to transform *a* into *b*. Transpositions of adjacent characters count as **two** edits (one deletion + one insertion). For transposition-aware distance, see [`similarity`](#similarity) which uses OSA distance internally.

#### Usage

```python
levenshtein_distance(a: str, b: str) -> int
```

**Parameters**

- `a` (str): First string.
- `b` (str): Second string.

**Returns**

- `int`: Non-negative edit distance. `0` means the strings are identical.

**Raises**

- `TypeError`: If either argument is not a `str`.

**Examples**

```python
from funcbox import levenshtein_distance

print(levenshtein_distance("kitten", "sitting"))
# 3

print(levenshtein_distance("hello", "hello"))
# 0

print(levenshtein_distance("dijktra", "dijkstra"))  # 1 substitution
# 1

print(levenshtein_distance("", "abc"))
# 3
```

---

### `is_anagram(str1, str2, case=False, spaces=False, punct=False)`

<a id="isanagram"></a>

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

### `is_null_or_blank(value)`

<a id="is_null_or_blank"></a>

Returns `True` if *value* is `None`, a whitespace-only string (or empty string), or an empty collection. Emptiness for collections is detected via `len()`, which is O(1) for all built-in types. Returns `False` for non-empty collections, non-`None` non-`Sized` types, and strings with at least one non-whitespace character.

#### Usage

```python
is_null_or_blank(value: object) -> bool
```

**Parameters**

- `value` (object): Any value. `None`, `str`, and any [`Sized`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sized) (e.g. `list`, `dict`, `tuple`, `set`, `frozenset`, `bytes`, `bytearray`, or custom classes implementing `__len__`) are all evaluated.

**Returns**

- `bool`: `True` if `value` is:
    - `None`
    - An empty string (`""`) or a string of only whitespace.
    - Any empty `Sized` (i.e. `len(value) == 0`).

  `False` otherwise.

**Examples**

```python
from funcbox import is_null_or_blank

print(is_null_or_blank(None))
# True
print(is_null_or_blank("\t\n"))
# True
print(is_null_or_blank([]))
# True
print(is_null_or_blank([1, 2]))
# False
print(is_null_or_blank({}))
# True
```

---

### `truncate(text, max_length, suffix="...", *, word_boundary=False)`

<a id="truncate"></a>

Shortens *text* to at most *max_length* characters (including the suffix). If the text already fits, it is returned unchanged.

#### Usage

```python
truncate(text: str, max_length: int, suffix: str = "...", *, word_boundary: bool = False) -> str
```

**Parameters**

- `text` (str): The source string to truncate.
- `max_length` (int): Maximum total length of the result, including the suffix. Must be a positive integer ≥ `len(suffix)`.
- `suffix` (str): Appended after the cut. Defaults to `"..."`.
- `word_boundary` (bool): When `True`, the cut snaps back to the last whitespace so words are never split. Defaults to `False`.

**Returns**

- `str`: The original string if it fits, otherwise the truncated string with the suffix appended.

**Raises**

- `TypeError`: Raised if `text` or `suffix` is not a `str`, or `max_length` is not a plain `int`.
- `ValueError`: Raised if `max_length` is not positive or is shorter than `suffix`.

**Examples**

```python
from funcbox import truncate

print(truncate("Hello, world!", 8))
# 'Hello...'

print(truncate("Hello, world!", 13))   # fits — returned unchanged
# 'Hello, world!'

print(truncate("Hello, world!", 10, suffix="…"))
# 'Hello, wo…'

print(truncate("The quick brown fox", 12, word_boundary=True))
# 'The quick...'

print(truncate("The quick brown fox", 12))  # no word boundary
# 'The quick...'
```

---

### Data Utilities

---

### `dig(data)`

<a id="dig"></a>

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

Choose your path format based on your needs:

- `str` (dot-path): Most cases; numbers auto-convert to list indices (e.g., `"user.address.city"` or `"projects.0.name"`)
- `tuple`: Keys with dots, or explicit integer indices (e.g., `("user", "projects", 0, "name")`)
- `list`: Query multiple paths in one call (e.g., `["user.name", "user.age"]`)

**Methods and operations**

- `d(path)`: Get value at path, returns `None` if not found
- `d(path, default=x)`: Get value, return `x` if path fails
- `d(path, last=True)`: Return the deepest found value before a miss
- `d([paths...])`: Resolve multiple paths → returns an ordered `list` (same order as input; missing paths yield `None` or `default`)
- `d[path]`: Shorthand for `d(path)`
- `path in d`: Check if path exists (True even if value is `None`)
- `d.scope(path)`: Create a new Dig rooted at that sub-path

**Raises** (on lookup)

- `TypeError`: If `path` is not a `str`, `tuple`, or `list`; or if a multi-path list entry is not a `str` or `tuple`.
- `KeyError`: If `path` passed to `scope()` does not exist.
- `TypeError`: If the value at `path` passed to `scope()` is not a `dict`.

**Returns**

- `Any` - the resolved value for single-path lookups.
- `list[Any]` - values aligned position-for-position with the input paths for multi-path lookups; missing paths yield `None` (or `default`).
- `dig` - a new scoped instance when calling `scope()`.

**Examples**

##### Setup: wrap your nested dictionary

```python
from funcbox import Dig

data = {
  "user": {
    "name": "Aditya Prasad S",
    "handle": "Pu94X",
    "age": 19,
    "email": None,
    "address": {
      "city": "Kanyakumari",
      "state": "Tamil Nadu",
      "zip": "629000",
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

d = Dig(data)  # Wrap once, query as many times as you like
```

##### Basic lookups with dot-paths

```python
# Navigate nested dicts with dot notation
d("user.name")
# 'Aditya Prasad S'

d("user.address.city")
# 'Kanyakumari'
```

##### Access lists by index

```python
# Numeric segments in dot-paths become list indices
d("user.projects.0.name")
# 'funcBox'

d("user.projects.1.lang")
# 'Kotlin'
```

##### Handle missing keys gracefully

```python
# Without default, missing keys return None
d("user.phone")
# None

# With default, use a fallback value
d("user.phone", default="N/A")
# 'N/A'

# last=True returns the deepest value found before the miss
d("user.address.phone", last=True)
# {'city': 'Kanyakumari', 'state': 'Tamil Nadu', 'zip': '629000'}
```

##### Use tuple paths for explicit keys

```python
# Useful when keys contain dots, or to avoid string parsing
d(("user", "projects", 0, "stars"))
# 42
```

##### Subscript shorthand and membership tests

```python
# Square bracket shorthand for single lookups
d["user.age"]
# 19

# Test if a path exists (True even if value is None)
"user.email" in d
# True  (key exists, value is None)

"user.phone" in d
# False  (key doesn't exist)
```

##### Query multiple paths at once

```python
# Pass a list of paths to get results as an ordered list
d(["user.name", "user.handle", "user.age"])
# ['Aditya Prasad S', 'Pu94X', 19]

# Missing paths yield None (or the default) at the same position
d(["user.name", "user.phone", "user.age"])
# ['Aditya Prasad S', None, 19]

# Defaults apply to all paths in a multi-path query
d(["user.projects.0.name", "user.projects.1.name"], default="unknown")
# ['funcBox', 'InfiniKit']
```

##### Scope into sub-sections (avoid repeating paths)

```python
# Create a scoped Dig at a sub-node
addr = d.scope("user.address")

addr("city")           # Query relative to the scope
# 'Kanyakumari'

addr["zip"]            # Shorthand works too
# '629000'

addr(["city", "state", "zip"])  # Multi-path relative to scope
# ['Kanyakumari', 'Tamil Nadu', '629000']
```

##### Scope into list elements

```python
# Scoping works with list indices too
proj = d.scope("user.projects.0")

proj("name")
# 'funcBox'

proj("stars")
# 42
```

##### Nested scopes

```python
# Scope from a scope for deeply nested access
notif = d.scope("user.settings.notifications")

notif("email")  # Cleaner than: d("user.settings.notifications.email")
# True

notif("push")
# False
```

##### String representation

```python
# See the top-level keys of a Dig
repr(d)
# Dig({'user'})

# After scoping, see the keys at that level
addr = d.scope("user.address")
repr(addr)
# Dig({'city', 'state', 'zip'})
```

> [!NOTE]
> **JSON integration:** `Dig` only accepts Python `dict` objects. If you're working with JSON, parse it first using `json.loads()` or `json.load()`:
> ```python
> import json
> from funcbox import Dig
> 
> json_string = '{"user": {"name": "Aditya"}}'
> data = json.loads(json_string)  # Parse to dict first
> d = Dig(data)
> d("user.name")  # 'Aditya'
> ```

> [!NOTE] 
> Numeric string segments like `"0"` in a dot-path are automatically coerced to integer indices when the current node is a `list` or `tuple`. Use a `tuple` path with an `int` element (e.g. `("user", "projects", 0, "name")`) for unambiguous index access.

---


## Disclaimer

FuncBox is provided as-is for general use. The developers make no warranties or guarantees regarding its fitness for any particular purpose. Users are responsible for validating results for their specific use cases and testing thoroughly before production deployment.

## Contributing

Contributions are welcome! Fork the repository, make your changes, and submit a pull request. Please ensure contributions align with the project's coding standards and include appropriate documentation.

## Issues & Bug Reports

Found a bug or have a feature request? [Open an issue on GitHub](https://github.com/funcBox-i3/funcBox/issues). Please search existing issues first to avoid duplicates and provide a clear description with reproducible code. For security vulnerabilities, email the maintainers directly.

## License

Licensed under the **MIT License**. See [LICENSE](LICENSE) for details.


<div align="center">

**Copyright © 2026**

</div>