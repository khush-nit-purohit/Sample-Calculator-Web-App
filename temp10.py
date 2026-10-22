"""
Fibonacci Sequence Module.

This module provides multiple robust, high-performance implementations for computing
Fibonacci numbers and generating Fibonacci sequences, adhering strictly to PEP 8 standards.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Generator


def fibonacci_iterative(n: int) -> int:
    """
    Calculate the n-th Fibonacci number using an iterative O(n) approach.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        n (int): The index of the Fibonacci number (0-indexed, where F(0) = 0, F(1) = 1).

    Returns:
        int: The n-th Fibonacci number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Examples:
        >>> fibonacci_iterative(0)
        0
        >>> fibonacci_iterative(1)
        1
        >>> fibonacci_iterative(10)
        55
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"Index 'n' must be an integer, got {type(n).__name__}.")
    if n < 0:
        raise ValueError(f"Index 'n' must be non-negative, got {n}.")

    if n in (0, 1):
        return n

    prev, current = 0, 1
    for _ in range(2, n + 1):
        prev, current = current, prev + current

    return current


@lru_cache(maxsize=1024)
def fibonacci_memoized(n: int) -> int:
    """
    Calculate the n-th Fibonacci number using recursion with LRU caching.

    Time Complexity: O(n)
    Space Complexity: O(n) call stack & cache

    Args:
        n (int): The index of the Fibonacci number (0-indexed).

    Returns:
        int: The n-th Fibonacci number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"Index 'n' must be an integer, got {type(n).__name__}.")
    if n < 0:
        raise ValueError(f"Index 'n' must be non-negative, got {n}.")

    if n < 2:
        return n

    return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)


def fibonacci_matrix(n: int) -> int:
    """
    Calculate the n-th Fibonacci number in O(log n) time using fast matrix exponentiation.

    The state transformation is:
        [[1, 1], [1, 0]]^n = [[F(n+1), F(n)], [F(n), F(n-1)]]

    Time Complexity: O(log n)
    Space Complexity: O(log n) auxiliary stack

    Args:
        n (int): The index of the Fibonacci number (0-indexed).

    Returns:
        int: The n-th Fibonacci number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"Index 'n' must be an integer, got {type(n).__name__}.")
    if n < 0:
        raise ValueError(f"Index 'n' must be non-negative, got {n}.")

    if n == 0:
        return 0

    def _multiply_2x2(
        a: tuple[tuple[int, int], tuple[int, int]],
        b: tuple[tuple[int, int], tuple[int, int]],
    ) -> tuple[tuple[int, int], tuple[int, int]]:
        return (
            (
                a[0][0] * b[0][0] + a[0][1] * b[1][0],
                a[0][0] * b[0][1] + a[0][1] * b[1][1],
            ),
            (
                a[1][0] * b[0][0] + a[1][1] * b[1][0],
                a[1][0] * b[0][1] + a[1][1] * b[1][1],
            ),
        )

    def _power(
        matrix: tuple[tuple[int, int], tuple[int, int]],
        exp: int,
    ) -> tuple[tuple[int, int], tuple[int, int]]:
        result = ((1, 0), (0, 1))  # Identity matrix
        base = matrix

        while exp > 0:
            if exp % 2 == 1:
                result = _multiply_2x2(result, base)
            base = _multiply_2x2(base, base)
            exp //= 2

        return result

    transformation_matrix = ((1, 1), (1, 0))
    # matrix^n has F(n) at position [0][1] or [1][0]
    result_matrix = _power(transformation_matrix, n)
    return result_matrix[0][1]


def fibonacci_sequence(count: int) -> list[int]:
    """
    Generate a list of the first `count` numbers in the Fibonacci sequence.

    Args:
        count (int): Number of Fibonacci values to generate.

    Returns:
        list[int]: A list containing the Fibonacci sequence of length `count`.

    Raises:
        TypeError: If count is not an integer.
        ValueError: If count is negative.

    Examples:
        >>> fibonacci_sequence(0)
        []
        >>> fibonacci_sequence(5)
        [0, 1, 1, 2, 3]
    """
    if not isinstance(count, int) or isinstance(count, bool):
        raise TypeError(f"'count' must be an integer, got {type(count).__name__}.")
    if count < 0:
        raise ValueError(f"'count' must be non-negative, got {count}.")

    if count == 0:
        return []
    if count == 1:
        return [0]

    sequence = [0, 1]
    for _ in range(2, count):
        sequence.append(sequence[-1] + sequence[-2])

    return sequence


def fibonacci_stream() -> Generator[int, None, None]:
    """
    An infinite generator yielding Fibonacci numbers sequentially.

    Yields:
        int: The next Fibonacci number.

    Examples:
        >>> stream = fibonacci_stream()
        >>> [next(stream) for _ in range(7)]
        [0, 1, 1, 2, 3, 5, 8]
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    import doctest

    # 1. Run embedded doctests
    print("Running doctests...")
    doctest_results = doctest.testmod()
    print(f"Doctests passed: {doctest_results.failed == 0}")

    # 2. Demonstration & Cross-Implementation Verification
    print("\n--- Fibonacci Demonstration ---")
    n_terms = 10
    print(f"First {n_terms} terms: {fibonacci_sequence(n_terms)}")

    test_indices = [0, 1, 2, 5, 10, 20, 50]
    print("\nVerifying equivalence across implementations:")
    for idx in test_indices:
        val_iter = fibonacci_iterative(idx)
        val_memo = fibonacci_memoized(idx)
        val_matrix = fibonacci_matrix(idx)
        assert val_iter == val_memo == val_matrix, f"Mismatch at index {idx}!"
        print(f"F({idx:2d}) = {val_iter}")

    # 3. High-Performance Test: O(log n) Matrix Exponentiation on large n
    large_n = 500
    large_fib = fibonacci_matrix(large_n)
    print(f"\nF({large_n}) computed via matrix exponentiation ({len(str(large_fib))} digits):")
    print(f"{str(large_fib)[:30]}...{str(large_fib)[-10:]}")
    print("\nAll checks passed successfully!")
