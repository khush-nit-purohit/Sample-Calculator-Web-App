def fibonacci(n):
    """
    Calculates the nth Fibonacci number.

    The Fibonacci sequence is a series of numbers where each number is the sum
    of the two preceding ones, usually starting with 0 and 1.
    (e.g., 0, 1, 1, 2, 3, 5, 8, 13, ...)

    Args:
        n (int): The index of the desired Fibonacci number (non-negative integer).

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is a negative integer.
        TypeError: If n is not an integer.
    """
    # Validate input type: ensure n is an integer
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    
    # Validate input value: ensure n is non-negative
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    # Base case: The 0th Fibonacci number is 0
    elif n == 0:
        return 0
    
    # Base case: The 1st Fibonacci number is 1
    elif n == 1:
        return 1
    
    # Iterative approach for n > 1
    else:
        # Initialize the first two Fibonacci numbers
        a, b = 0, 1
        # Loop from the 2nd number up to the nth number
        for _ in range(2, n + 1):
            # Calculate the next Fibonacci number by summing the previous two
            # and update a and b for the next iteration
            a, b = b, a + b
        # Return the nth Fibonacci number
        return b

if __name__ == "__main__":
    # This block demonstrates the usage of the fibonacci function
    print("--- Fibonacci Sequence Examples ---")

    # Example 1: Calculate the 0th Fibonacci number
    try:
        print(f"Fibonacci(0): {fibonacci(0)}")  # Expected output: 0
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

    # Example 2: Calculate the 1st Fibonacci number
    try:
        print(f"Fibonacci(1): {fibonacci(1)}")  # Expected output: 1
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

    # Example 3: Calculate the 7th Fibonacci number
    try:
        print(f"Fibonacci(7): {fibonacci(7)}")  # Expected output: 13
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

    # Example 4: Calculate the 10th Fibonacci number
    try:
        print(f"Fibonacci(10): {fibonacci(10)}") # Expected output: 55
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

    # Example 5: Test with a larger number, the 20th Fibonacci number
    try:
        print(f"Fibonacci(20): {fibonacci(20)}") # Expected output: 6765
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

    print("
--- Error Handling Examples ---")

    # Example 6: Test with a negative input to trigger ValueError
    try:
        print(f"Fibonacci(-5): {fibonacci(-5)}")
    except (ValueError, TypeError) as e:
        print(f"Caught expected error for negative input: {e}")

    # Example 7: Test with a non-integer input (float) to trigger TypeError
    try:
        print(f"Fibonacci(3.5): {fibonacci(3.5)}")
    except (ValueError, TypeError) as e:
        print(f"Caught expected error for float input: {e}")

    # Example 8: Test with a non-integer input (string) to trigger TypeError
    try:
        print(f"Fibonacci('abc'): {fibonacci('abc')}")
    except (ValueError, TypeError) as e:
        print(f"Caught expected error for string input: {e}")