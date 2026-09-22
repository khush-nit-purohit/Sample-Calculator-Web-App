"""
fibonacci_generator.py

This module provides a function to generate a Fibonacci sequence up to a specified
number of terms. The Fibonacci sequence is a series of numbers where each number
is the sum of the two preceding ones, usually starting with 0 and 1.

Example: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
"""

def generate_fibonacci_sequence(n: int) -> list[int]:
    """
    Generates the first 'n' Fibonacci numbers.

    The Fibonacci sequence starts with 0 and 1, and each subsequent number
    is the sum of the two preceding ones.

    Args:
        n (int): The number of Fibonacci terms to generate.
                 Must be a non-negative integer.

    Returns:
        list[int]: A list containing the first 'n' Fibonacci numbers.

    Raises:
        ValueError: If 'n' is a negative integer.

    Examples:
        >>> generate_fibonacci_sequence(0)
        []
        >>> generate_fibonacci_sequence(1)
        [0]
        >>> generate_fibonacci_sequence(2)
        [0, 1]
        >>> generate_fibonacci_sequence(5)
        [0, 1, 1, 2, 3]
        >>> generate_fibonacci_sequence(10)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
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
    fib_sequence = [0, 1]

    # Generate subsequent terms iteratively
    # We already have 2 terms, so we iterate n-2 times
    for _ in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    return fib_sequence

# --- Example Usage and Demonstration ---
if __name__ == "__main__":
    print("--- Fibonacci Sequence Generator ---")

    # Test cases with various inputs
    test_cases = [0, 1, 2, 5, 10, 15, 20]

    for num_terms in test_cases:
        try:
            sequence = generate_fibonacci_sequence(num_terms)
            print(f"Fibonacci sequence for n = {num_terms}: {sequence}")
        except (ValueError, TypeError) as e:
            print(f"Error generating sequence for n = {num_terms}: {e}")

    print("
--- Testing Edge Cases and Error Handling ---")

    # Test with a negative number
    try:
        print(f"Fibonacci sequence for n = -5: {generate_fibonacci_sequence(-5)}")
    except (ValueError, TypeError) as e:
        print(f"Error generating sequence for n = -5: {e}")

    # Test with a non-integer input
    try:
        print(f"Fibonacci sequence for n = 3.5: {generate_fibonacci_sequence(3.5)}")
    except (ValueError, TypeError) as e:
        print(f"Error generating sequence for n = 3.5: {e}")

    # Test with a large number (demonstrates efficiency of iterative approach)
    large_n = 50
    print(f"
Fibonacci sequence for n = {large_n} (first 10 terms shown):")
    large_sequence = generate_fibonacci_sequence(large_n)
    print(large_sequence[:10], "...", large_sequence[-1]) # Print first 10 and the last term
    print(f"Length of sequence: {len(large_sequence)}")