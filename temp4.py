def fibonacci_sequence(n):
    """
    Generates a list containing the first 'n' Fibonacci numbers.

    The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones,
    usually starting with 0 and 1.

    Args:
        n (int): The number of Fibonacci terms to generate.
                 Must be a non-negative integer.

    Returns:
        list: A list of the first 'n' Fibonacci numbers.
              Returns an empty list if n is 0 or less.
              Returns [0] if n is 1.
              Returns [0, 1] if n is 2.
    """
    # Handle edge case: if n is less than or equal to 0, return an empty list
    if n <= 0:
        return []
    # Handle edge case: if n is 1, return a list containing only the first Fibonacci number (0)
    elif n == 1:
        return [0]
    # Handle edge case: if n is 2, return a list containing the first two Fibonacci numbers (0, 1)
    elif n == 2:
        return [0, 1]
    else:
        # Initialize the list with the first two Fibonacci numbers
        # This is the starting point for generating the sequence
        sequence = [0, 1]
        # Loop from the 3rd term up to the 'n'th term
        # We start from 2 because the first two terms (index 0 and 1) are already in 'sequence'
        for i in range(2, n):
            # Calculate the next Fibonacci number by summing the previous two
            # sequence[i-1] is the immediately preceding number
            # sequence[i-2] is the number before the immediately preceding one
            next_fib = sequence[i - 1] + sequence[i - 2]
            # Add the newly calculated Fibonacci number to the sequence list
            sequence.append(next_fib)
        # Return the complete list of Fibonacci numbers
        return sequence

def fibonacci_nth(n):
    """
    Calculates the 'n'th Fibonacci number.

    This function uses an iterative approach to find the Fibonacci number at a specific position.
    The sequence is typically considered to start with F(0) = 0, F(1) = 1, F(2) = 1, etc.

    Args:
        n (int): The position of the Fibonacci number to calculate (0-indexed).
                 Must be a non-negative integer.

    Returns:
        int: The 'n'th Fibonacci number.
             Returns 0 if n is 0.
             Returns 1 if n is 1.
             Returns -1 if n is negative (as Fibonacci is typically defined for non-negative integers).
    """
    # Handle edge case: if n is negative, return -1 as Fibonacci is not typically defined for negative indices
    if n < 0:
        return -1
    # Handle base case: the 0th Fibonacci number is 0
    elif n == 0:
        return 0
    # Handle base case: the 1st Fibonacci number is 1
    elif n == 1:
        return 1
    else:
        # Initialize the first two Fibonacci numbers
        # 'a' holds the (n-2)th Fibonacci number
        # 'b' holds the (n-1)th Fibonacci number
        a, b = 0, 1
        # Loop from the 2nd position up to the 'n'th position
        # We've already handled 0 and 1, so we start calculating from the 2nd term
        for _ in range(2, n + 1):
            # Calculate the next Fibonacci number
            # The new 'a' becomes the old 'b'
            # The new 'b' becomes the sum of the old 'a' and 'b'
            a, b = b, a + b
        # After the loop, 'b' will hold the 'n'th Fibonacci number
        return b

# --- Example Usage ---
if __name__ == "__main__":
    print("--- Fibonacci Sequence Generation ---")

    # Example 1: Generate the first 10 Fibonacci numbers
    num_terms_1 = 10
    # Call the fibonacci_sequence function with num_terms_1
    fib_list_1 = fibonacci_sequence(num_terms_1)
    # Print the result in a user-friendly format
    print(f"The first {num_terms_1} Fibonacci numbers are: {fib_list_1}")
    # Expected output: The first 10 Fibonacci numbers are: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    # Example 2: Generate the first 1 Fibonacci number (edge case)
    num_terms_2 = 1
    fib_list_2 = fibonacci_sequence(num_terms_2)
    print(f"The first {num_terms_2} Fibonacci number is: {fib_list_2}")
    # Expected output: The first 1 Fibonacci number is: [0]

    # Example 3: Generate 0 Fibonacci numbers (edge case)
    num_terms_3 = 0
    fib_list_3 = fibonacci_sequence(num_terms_3)
    print(f"The first {num_terms_3} Fibonacci numbers are: {fib_list_3}")
    # Expected output: The first 0 Fibonacci numbers are: []

    print("
--- Nth Fibonacci Number Calculation ---")

    # Example 4: Find the 0th Fibonacci number
    nth_term_1 = 0
    # Call the fibonacci_nth function with nth_term_1
    fib_nth_1 = fibonacci_nth(nth_term_1)
    # Print the result
    print(f"The {nth_term_1}th Fibonacci number is: {fib_nth_1}")
    # Expected output: The 0th Fibonacci number is: 0

    # Example 5: Find the 1st Fibonacci number
    nth_term_2 = 1
    fib_nth_2 = fibonacci_nth(nth_term_2)
    print(f"The {nth_term_2}st Fibonacci number is: {fib_nth_2}")
    # Expected output: The 1st Fibonacci number is: 1

    # Example 6: Find the 7th Fibonacci number
    nth_term_3 = 7
    fib_nth_3 = fibonacci_nth(nth_term_3)
    print(f"The {nth_term_3}th Fibonacci number is: {fib_nth_3}")
    # Expected output: The 7th Fibonacci number is: 13 (0, 1, 1, 2, 3, 5, 8, 13)

    # Example 7: Find a negative indexed Fibonacci number (edge case)
    nth_term_4 = -5
    fib_nth_4 = fibonacci_nth(nth_term_4)
    print(f"The {nth_term_4}th Fibonacci number is: {fib_nth_4}")
    # Expected output: The -5th Fibonacci number is: -1 (indicating an invalid input)