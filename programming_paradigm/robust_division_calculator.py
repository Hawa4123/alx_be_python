<<<<<<< HEAD
def safe_divide(numerator, denominator):
    """Performs safe division and handles errors."""
    try:
        num = float(numerator)
        den = float(denominator)
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
=======
def safe_divide(numerator, denominator):
    """Performs safe division and handles errors."""
    try:
        num = float(numerator)
        den = float(denominator)
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
>>>>>>> a36e86f0eac74d6801fdd3e4d6f1ad6fde9c4c3d
