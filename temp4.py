def fibonacci(n: int) -> int:
    """
    Calculates the nth Fibonacci number.

    The Fibonacci sequence is a series of numbers where each number is the sum
    of the two preceding ones, usually starting with 0 and 1.
    (e.g., 0, 1, 1, 2, 3, 5, 8, 13, ...)

    This implementation uses an iterative approach for efficiency,
    avoiding the potential performance issues and recursion depth limits
    associated with a naive recursive solution for larger 'n'.

    Args:
        n: The position of the desired Fibonacci number in the sequence.
           Must be a non-negative integer.

    Returns:
        The nth Fibonacci number.

    Raises:
        ValueError: If n is a negative integer.
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("Input 'n' must be an integer.")
    if n < 0:
        raise ValueError("Input 'n' cannot be a negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        # Iterate n-1 times because we already handled n=0 and n=1
        # and started with the first two numbers (a=0, b=1).
        # The loop will calculate from the 2nd Fibonacci number onwards.
        for _ in range(2, n + 1):
            next_fib = a + b
            a = b
            b = next_fib
        return b

if __name__ == "__main__":
    print("--- Fibonacci Sequence Examples ---")

    # Example 1: First few Fibonacci numbers
    print("\nCalculating the first 10 Fibonacci numbers:")
    for i in range(11):  # From 0 to 10
        print(f"fibonacci({i}) = {fibonacci(i)}")

    # Example 2: A larger Fibonacci number
    n_large = 20
    print(f"\nCalculating fibonacci({n_large}):")
    print(f"fibonacci({n_large}) = {fibonacci(n_large)}")

    # Example 3: Edge cases
    print("\nTesting edge cases:")
    print(f"fibonacci(0) = {fibonacci(0)}")
    print(f"fibonacci(1) = {fibonacci(1)}")

    # Example 4: Error handling for negative input
    print("\nTesting error handling for negative input:")
    try:
        fibonacci(-5)
    except ValueError as e:
        print(f"Caught expected error: {e}")

    # Example 5: Error handling for non-integer input
    print("\nTesting error handling for non-integer input:")
    try:
        fibonacci(3.14)
    except TypeError as e:
        print(f"Caught expected error: {e}")
