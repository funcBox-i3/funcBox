from .algorithms import binary_search, dijkstra, primes
from .classify_numbers import classify_numbers
from .fibonacci import fibonacci
from .get_factors import get_factors
from .is_anagram import is_anagram
from .is_prime import is_prime
from .safe_get import safe_get

__all__ = [
    "binary_search",
    "classify_numbers",
    "dijkstra",
    "fibonacci",
    "get_factors",
    "is_anagram",
    "is_prime",
    "primes",
    "safe_get",
]

# Aliases
# fact = factorial

__version__ = "0.3.2"
