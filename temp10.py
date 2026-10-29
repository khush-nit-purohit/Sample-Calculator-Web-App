"""
Module: decimal_to_hex_converter
Description: A robust, production-grade decimal-to-hexadecimal conversion library
             and CLI utility. It implements conversion from first principles
             (successive division and multiplication algorithms) while offering
             support for integer signed formats, two's complement, fixed-point
             floating-point representations, padding, and case formatting.
Adheres strictly to PEP 8 guidelines.
"""

from __future__ import annotations
import sys
import unittest
from typing import Final, Optional


class DecimalToHexConverter:
    """
    Provides algorithmic conversion utilities between decimal values (integers
    and floating-point numbers) and their hexadecimal string representations.
    """

    HEX_DIGITS_UPPER: Final[str] = "0123456789ABCDEF"
    HEX_DIGITS_LOWER: Final[str] = "0123456789abcdef"

    @classmethod
    def convert_integer(
        cls,
        number: int,
        *,
        uppercase: bool = True,
        include_prefix: bool = True,
        min_width: int = 1,
        twos_complement_bits: Optional[int] = None,
    ) -> str:
        """
        Converts a decimal integer to its hexadecimal string representation
        using the successive division-by-16 algorithm.

        Algorithm:
            1. Repeatedly divide the magnitude of the integer by 16.
            2. The remainder of each division maps to a hexadecimal digit (0-F).
            3. The quotient becomes the input for the subsequent division step.
            4. The process repeats until quotient is 0.
            5. Reversing the collected remainder digits produces the hexadecimal value.

        Args:
            number: The integer to convert (positive, negative, or zero).
            uppercase: If True, uses uppercase letters ('A'-'F') and prefix '0X'.
                       If False, uses lowercase letters ('a'-'f') and prefix '0x'.
            include_prefix: If True, prepends the radix prefix ('0x' or '0X').
            min_width: Minimum number of hex digits in the output (padded with leading zeros).
            twos_complement_bits: Optional bit-width (e.g., 8, 16, 32, 64) to format
                                  negative integers using two's complement representation.
                                  Must be a positive multiple of 4.

        Returns:
            str: Hexadecimal string representation.

        Raises:
            TypeError: If `number` or `min_width` is not an integer.
            ValueError: If `min_width` < 1 or `twos_complement_bits` is invalid.
            OverflowError: If `number` does not fit inside the specified two's complement bit-width.
        """
        # Validate inputs
        if not isinstance(number, int):
            raise TypeError(
                f"Expected integer for 'number', got {type(number).__name__}."
            )
        if not isinstance(min_width, int) or min_width < 1:
            raise ValueError("'min_width' must be a positive integer >= 1.")

        hex_chars = cls.HEX_DIGITS_UPPER if uppercase else cls.HEX_DIGITS_LOWER

        # Handle Two's Complement representation when requested
        if twos_complement_bits is not None:
            if not isinstance(twos_complement_bits, int) or twos_complement_bits <= 0 or twos_complement_bits % 4 != 0:
                raise ValueError(
                    "'twos_complement_bits' must be a positive multiple of 4 (e.g., 8, 16, 32, 64)."
                )

            min_val = -(1 << (twos_complement_bits - 1))
            max_val = (1 << (twos_complement_bits - 1)) - 1

            if not (min_val <= number <= max_val):
                raise OverflowError(
                    f"Number {number} cannot be represented in a signed {twos_complement_bits}-bit "
                    f"range [{min_val}, {max_val}]."
                )

            # Bitwise mask captures standard two's complement bit pattern
            working_value = number & ((1 << twos_complement_bits) - 1)
            is_negative = False
            # Ensure width corresponds to the bit size (4 bits per hex nibble)
            min_width = max(min_width, twos_complement_bits // 4)
        else:
            is_negative = number < 0
            working_value = abs(number)

        # Core Division-Remainder Algorithm
        if working_value == 0:
            hex_body = "0"
        else:
            digit_collector = []
            quotient = working_value
            while quotient > 0:
                remainder = quotient % 16
                digit_collector.append(hex_chars[remainder])
                quotient //= 16
            hex_body = "".join(reversed(digit_collector))

        # Pad with leading zeros if specified
        if len(hex_body) < min_width:
            hex_body = hex_body.zfill(min_width)

        # Build final formatted representation
        prefix = ("0X" if uppercase else "0x") if include_prefix else ""

        if is_negative:
            return f"-{prefix}{hex_body}"
        return f"{prefix}{hex_body}"

    @classmethod
    def convert_float(
        cls,
        number: float,
        *,
        precision: int = 6,
        uppercase: bool = True,
        include_prefix: bool = True,
    ) -> str:
        """
        Converts a decimal floating-point number into a fixed-point hexadecimal string.

        Algorithm for Fractional Part:
            1. Multiply fractional component by 16.
            2. The integer part of the product represents the next hexadecimal digit.
            3. The new fractional part is carried over into the next iteration.
            4. Repeat until fraction equals 0.0 or specified precision is reached.

        Args:
            number: Decimal float or int to convert.
            precision: Maximum number of fractional hexadecimal digits to calculate.
            uppercase: If True, uses '0X' and 'A-F'; otherwise '0x' and 'a-f'.
            include_prefix: If True, adds '0x' or '0X' prefix.

        Returns:
            str: Fixed-point hexadecimal representation (e.g. 10.625 -> "0XA.A").
        """
        if not isinstance(number, (int, float)):
            raise TypeError(
                f"Expected int or float for 'number', got {type(number).__name__}."
            )
        if not isinstance(precision, int) or precision < 0:
            raise ValueError("'precision' must be a non-negative integer.")

        is_negative = number < 0
        abs_val = abs(float(number))

        integer_part = int(abs_val)
        fractional_part = abs_val - integer_part

        hex_chars = cls.HEX_DIGITS_UPPER if uppercase else cls.HEX_DIGITS_LOWER

        # Convert whole number component
        int_hex = cls.convert_integer(
            integer_part,
            uppercase=uppercase,
            include_prefix=False
        )

        # Convert fractional component using successive multiplication
        frac_digits = []
        current_fraction = fractional_part

        for _ in range(precision):
            if current_fraction == 0.0:
                break
            current_fraction *= 16
            digit = int(current_fraction)
            frac_digits.append(hex_chars[digit])
            current_fraction -= digit

        frac_hex = "".join(frac_digits)
        body = f"{int_hex}.{frac_hex}" if frac_hex else int_hex
        prefix = ("0X" if uppercase else "0x") if include_prefix else ""

        if is_negative:
            return f"-{prefix}{body}"
        return f"{prefix}{body}"


# Convenient module-level aliases
decimal_to_hex = DecimalToHexConverter.convert_integer
decimal_float_to_hex = DecimalToHexConverter.convert_float


# ============================================================================
# Unit Tests & Verification
# ============================================================================

class TestDecimalToHexConverter(unittest.TestCase):
    """Automated unit test suite verifying accuracy and boundary conditions."""

    def test_zero_conversion(self):
        self.assertEqual(decimal_to_hex(0), "0X0")
        self.assertEqual(decimal_to_hex(0, include_prefix=False), "0")
        self.assertEqual(decimal_to_hex(0, min_width=4), "0X0000")

    def test_standard_positive_integers(self):
        self.assertEqual(decimal_to_hex(10), "0XA")
        self.assertEqual(decimal_to_hex(15), "0XF")
        self.assertEqual(decimal_to_hex(16), "0X10")
        self.assertEqual(decimal_to_hex(255), "0XFF")
        self.assertEqual(decimal_to_hex(4096), "0X1000")
        self.assertEqual(decimal_to_hex(255, uppercase=False), "0xff")

    def test_negative_sign_magnitude(self):
        self.assertEqual(decimal_to_hex(-1), "-0X1")
        self.assertEqual(decimal_to_hex(-255), "-0XFF")
        self.assertEqual(decimal_to_hex(-255, include_prefix=False), "-FF")

    def test_twos_complement_representation(self):
        self.assertEqual(decimal_to_hex(-1, twos_complement_bits=8), "0XFF")
        self.assertEqual(decimal_to_hex(-1, twos_complement_bits=16), "0XFFFF")
        self.assertEqual(decimal_to_hex(-128, twos_complement_bits=8), "0X80")
        self.assertEqual(decimal_to_hex(127, twos_complement_bits=8), "0X7F")

        # Test out-of-bounds error
        with self.assertRaises(OverflowError):
            decimal_to_hex(128, twos_complement_bits=8)

    def test_fractional_conversion(self):
        self.assertEqual(decimal_float_to_hex(10.625), "0XA.A")
        self.assertEqual(decimal_float_to_hex(-42.125), "-0X2A.2")
        self.assertEqual(decimal_float_to_hex(0.0), "0X0")
        self.assertEqual(decimal_float_to_hex(255.0), "0XFF")

    def test_type_and_value_errors(self):
        with self.assertRaises(TypeError):
            decimal_to_hex("123")  # type: ignore
        with self.assertRaises(ValueError):
            decimal_to_hex(10, min_width=0)
        with self.assertRaises(ValueError):
            decimal_to_hex(10, twos_complement_bits=5)


# ============================================================================
# Main Demonstration Runner
# ============================================================================

def main() -> None:
    """Executes demonstrations and runs the test suite."""
    print("=" * 70)
    print("      DECIMAL TO HEXADECIMAL CONVERSION DEMONSTRATION")
    print("=" * 70)

    sample_integers = [0, 9, 10, 15, 16, 255, 1024, 65535, 1048575, -42, -255]

    print("\n[1] Basic Integer Conversions:")
    print(f"{'Decimal':<12} | {'Hex (Upper)':<14} | {'Hex (Lower)':<14} | {'Raw (No Prefix)':<16}")
    print("-" * 65)
    for num in sample_integers:
        hex_up = decimal_to_hex(num, uppercase=True, include_prefix=True)
        hex_low = decimal_to_hex(num, uppercase=False, include_prefix=True)
        hex_raw = decimal_to_hex(num, uppercase=True, include_prefix=False)
        print(f"{num:<12} | {hex_up:<14} | {hex_low:<14} | {hex_raw:<16}")

    print("\n[2] Formatting with Padding (min_width=4):")
    for num in [0, 5, 255, 4095]:
        padded = decimal_to_hex(num, min_width=4)
        print(f"Decimal {num:<5} -> {padded}")

    print("\n[3] Two's Complement Signed Format (8-bit and 16-bit):")
    sample_twos = [-1, -2, -128, 127]
    for num in sample_twos:
        hex_8bit = decimal_to_hex(num, twos_complement_bits=8)
        hex_16bit = decimal_to_hex(num, twos_complement_bits=16)
        print(f"Decimal {num:<5} -> 8-bit: {hex_8bit} | 16-bit: {hex_16bit}")

    print("\n[4] Fixed-Point Floating-Point Conversions:")
    sample_floats = [10.625, 0.125, 255.5, -42.125, 0.2]
    for f in sample_floats:
        print(f"Float {f:<8} -> {decimal_float_to_hex(f, precision=4)}")

    print("\n" + "=" * 70)
    print("Running Integrated Unit Tests...")
    print("=" * 70)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDecimalToHexConverter)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if not result.wasSuccessful():
        sys.exit(1)


if __name__ == "__main__":
    main()
