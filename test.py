"""
fibonacci_generator.py

This module provides a function to generate the Fibonacci sequence up to a specified
number of terms. The Fibonacci sequence is a series of numbers where each number
is the sum of the two preceding ones, usually starting with 0 and 1.

Example: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
"""

def fibonacci_sequence(n: int) -> list[int]:
    """
    Generates the first 'n' numbers of the Fibonacci sequence.

    The Fibonacci sequence starts with 0 and 1, and each subsequent number
    is the sum of the two preceding ones.

    Args:
        n (int): The number of Fibonacci terms to generate.
                 Must be a non-negative integer.

    Returns:
        list[int]: A list containing the first 'n' Fibonacci numbers.
                   Returns an empty list if n is 0.

    Raises:
        ValueError: If 'n' is a negative integer.

    Examples:
        >>> fibonacci_sequence(0)
        []
        >>> fibonacci_sequence(1)
        [0]
        >>> fibonacci_sequence(2)
        [0, 1]
        >>> fibonacci_sequence(7)
        [0, 1, 1, 2, 3, 5, 8]
    """
    if not isinstance(n, int):
        raise TypeError("Input 'n' must be an integer.")
    if n < 0:
        raise ValueError("Input 'n' must be a non-negative integer.")

    # Handle base cases for the Fibonacci sequence
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    # Initialize the sequence with the first two terms
    sequence = [0, 1]

    # Generate subsequent terms iteratively
    # We already have 2 terms, so we need to generate n-2 more terms
    for _ in range(2, n):
        next_fib = sequence[-1] + sequence[-2]
        sequence.append(next_fib)

    return sequence

# --- Example Usage ---
if __name__ == "__main__":
    print("--- Fibonacci Sequence Generator ---")

    # Test cases for various inputs
    test_cases = [0, 1, 2, 5, 10, 15]

    for num_terms in test_cases:
        try:
            fib_series = fibonacci_sequence(num_terms)
            print(f"First {num_terms} Fibonacci numbers: {fib_series}")
        except (ValueError, TypeError) as e:
            print(f"Error generating Fibonacci for {num_terms}: {e}")

    # Test with an invalid input (negative number)
    print("
--- Testing with invalid input (negative) ---")
    try:
        fib_series_negative = fibonacci_sequence(-5)
        print(f"First -5 Fibonacci numbers: {fib_series_negative}")
    except (ValueError, TypeError) as e:
        print(f"Caught expected error for negative input: {e}")

    # Test with an invalid input (non-integer)
    print("
--- Testing with invalid input (non-integer) ---")
    try:
        fib_series_float = fibonacci_sequence(5.5)
        print(f"First 5.5 Fibonacci numbers: {fib_series_float}")
    except (ValueError, TypeError) as e:
        print(f"Caught expected error for non-integer input: {e}")

    print("
--- End of Demonstration ---")