def fibonacci(n):
    """
    Calculates the nth Fibonacci number.

    The Fibonacci sequence is a series of numbers where each number is the sum
    of the two preceding ones, usually starting with 0 and 1.
    (e.g., 0, 1, 1, 2, 3, 5, 8, 13, ...)

    Args:
        n (int): The index of the desired Fibonacci number.
                 Must be a non-negative integer.

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is a negative integer.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def generate_fibonacci_sequence(count):
    """
    Generates a list containing the first 'count' Fibonacci numbers.

    Args:
        count (int): The number of Fibonacci numbers to generate.
                     Must be a non-negative integer.

    Returns:
        list: A list of the first 'count' Fibonacci numbers.

    Raises:
        ValueError: If count is a negative integer.
    """
    if not isinstance(count, int):
        raise TypeError("Input must be an integer.")
    if count < 0:
        raise ValueError("Input must be a non-negative integer.")

    sequence = []
    for i in range(count):
        sequence.append(fibonacci(i))
    return sequence

if __name__ == "__main__":
    print("--- Fibonacci Number Calculation ---")
    try:
        # Example: Calculate the 10th Fibonacci number
        n_value = 10
        fib_number = fibonacci(n_value)
        print(f"The {n_value}th Fibonacci number is: {fib_number}")

        # Example: Calculate the 0th Fibonacci number
        n_value = 0
        fib_number = fibonacci(n_value)
        print(f"The {n_value}th Fibonacci number is: {fib_number}")

        # Example: Calculate the 1st Fibonacci number
        n_value = 1
        fib_number = fibonacci(n_value)
        print(f"The {n_value}st Fibonacci number is: {fib_number}")

        # Example with a larger number
        n_value = 20
        fib_number = fibonacci(n_value)
        print(f"The {n_value}th Fibonacci number is: {fib_number}")

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

    print("
--- Fibonacci Sequence Generation ---")
    try:
        # Example: Generate the first 15 Fibonacci numbers
        count_value = 15
        fib_sequence = generate_fibonacci_sequence(count_value)
        print(f"The first {count_value} Fibonacci numbers are: {fib_sequence}")

        # Example: Generate the first 5 Fibonacci numbers
        count_value = 5
        fib_sequence = generate_fibonacci_sequence(count_value)
        print(f"The first {count_value} Fibonacci numbers are: {fib_sequence}")

        # Example: Generate 0 Fibonacci numbers
        count_value = 0
        fib_sequence = generate_fibonacci_sequence(count_value)
        print(f"The first {count_value} Fibonacci numbers are: {fib_sequence}")

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

    print("
--- Error Handling Examples ---")
    try:
        fibonacci(-5)
    except (ValueError, TypeError) as e:
        print(f"Caught expected error for fibonacci(-5): {e}")

    try:
        fibonacci(3.5)
    except (ValueError, TypeError) as e:
        print(f"Caught expected error for fibonacci(3.5): {e}")

    try:
        generate_fibonacci_sequence(-3)
    except (ValueError, TypeError) as e:
        print(f"Caught expected error for generate_fibonacci_sequence(-3): {e}")

    try:
        generate_fibonacci_sequence("ten")
    except (ValueError, TypeError) as e:
        print(f"Caught expected error for generate_fibonacci_sequence("ten"): {e}")