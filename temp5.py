"""
fibonacci_generator.py

This module provides functions to generate the Fibonacci sequence.
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones,
usually starting with 0 and 1.

F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2) for n > 1

This implementation uses an iterative approach for efficiency, avoiding the
performance issues (redundant calculations) often associated with naive recursive solutions
for larger 'n' values.
"""

def generate_fibonacci_sequence(n: int) -> list[int]:
    """
    Generates the first 'n' Fibonacci numbers.

    This function calculates the Fibonacci sequence iteratively, which is
    more efficient than a naive recursive approach for larger 'n' values
    as it avoids repeated calculations.

    Args:
        n (int): The number of Fibonacci numbers to generate.
                 Must be a non-negative integer.

    Returns:
        list[int]: A list containing the first 'n' Fibonacci numbers.
                   Returns an empty list if n is 0.

    Raises:
        ValueError: If 'n' is a negative integer.

    Example:
        >>> generate_fibonacci_sequence(0)
        []
        >>> generate_fibonacci_sequence(1)
        [0]
        >>> generate_fibonacci_sequence(5)
        [0, 1, 1, 2, 3]
        >>> generate_fibonacci_sequence(10)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    if not isinstance(n, int):
        raise TypeError("Input 'n' must be an integer.")
    if n < 0:
        raise ValueError("Input 'n' must be a non-negative integer.")

    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        # Initialize the sequence with the first two Fibonacci numbers
        fib_sequence = [0, 1]
        # Generate subsequent numbers up to 'n'
        # We already have 2 numbers, so we iterate n-2 times
        for _ in range(2, n):
            next_fib = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_fib)
        return fib_sequence

def get_nth_fibonacci(n: int) -> int:
    """
    Calculates the nth Fibonacci number (0-indexed).

    This function calculates a specific Fibonacci number iteratively.
    F(0) = 0, F(1) = 1, F(2) = 1, F(3) = 2, etc.

    Args:
        n (int): The index of the Fibonacci number to retrieve.
                 Must be a non-negative integer.

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If 'n' is a negative integer.

    Example:
        >>> get_nth_fibonacci(0)
        0
        >>> get_nth_fibonacci(1)
        1
        >>> get_nth_fibonacci(5)
        5
        >>> get_nth_fibonacci(10)
        55
    """
    if not isinstance(n, int):
        raise TypeError("Input 'n' must be an integer.")
    if n < 0:
        raise ValueError("Input 'n' must be a non-negative integer.")

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        # Iterate n-1 times to reach the nth number
        # (since we already have F(0) and F(1))
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# --- Example Usage and Test Cases ---
if __name__ == "__main__":
    print("--- Fibonacci Sequence Generator ---")

    # Test cases for generate_fibonacci_sequence
    print("
Testing generate_fibonacci_sequence(n):")
    test_cases_sequence = [0, 1, 2, 5, 10, 15]
    for num in test_cases_sequence:
        try:
            sequence = generate_fibonacci_sequence(num)
            print(f"First {num} Fibonacci numbers: {sequence}")
        except (ValueError, TypeError) as e:
            print(f"Error for n={num}: {e}")

    # Test edge cases for generate_fibonacci_sequence
    print("
Testing edge cases for generate_fibonacci_sequence:")
    try:
        print(f"First -5 Fibonacci numbers: {generate_fibonacci_sequence(-5)}")
    except (ValueError, TypeError) as e:
        print(f"Error for n=-5: {e}")

    try:
        print(f"First 'abc' Fibonacci numbers: {generate_fibonacci_sequence('abc')}")
    except (ValueError, TypeError) as e:
        print(f"Error for n='abc': {e}")

    # Test cases for get_nth_fibonacci
    print("
--- Nth Fibonacci Number Calculator ---")
    print("
Testing get_nth_fibonacci(n):")
    test_cases_nth = [0, 1, 2, 5, 10, 20]
    for num in test_cases_nth:
        try:
            nth_fib = get_nth_fibonacci(num)
            print(f"The {num}th Fibonacci number is: {nth_fib}")
        except (ValueError, TypeError) as e:
            print(f"Error for n={num}: {e}")

    # Test edge cases for get_nth_fibonacci
    print("
Testing edge cases for get_nth_fibonacci:")
    try:
        print(f"The -3rd Fibonacci number: {get_nth_fibonacci(-3)}")
    except (ValueError, TypeError) as e:
        print(f"Error for n=-3: {e}")

    try:
        print(f"The 'xyz'th Fibonacci number: {get_nth_fibonacci('xyz')}")
    except (ValueError, TypeError) as e:
        print(f"Error for n='xyz': {e}")

    print("
--- Demonstration Complete ---")