import unittest

# Define the calculator functions
def add(a, b):
    return a + b

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

class TestCalculatorFunctions(unittest.TestCase):

    # Test cases for the add function
    def test_add_positive_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 5, "Adding positive numbers")

    def test_add_negative_numbers(self):
        result = add(-1, 1)
        self.assertEqual(result, 0, "Adding negative numbers")

    def test_add_zeros(self):
        result = add(0, 0)
        self.assertEqual(result, 0, "Adding zeros")

    # Test cases for the subtract function
    def test_subtract_positive_numbers(self):
        result = subtract(3, 2)
        self.assertEqual(result, 1, "Subtracting positive numbers")

    def test_subtract_negative_numbers(self):
        result = subtract(-1, 1)
        self.assertEqual(result, -2, "Subtracting negative numbers")

    def test_subtract_zeros(self):
        result = subtract(0, 0)
        self.assertEqual(result, 0, "Subtracting zeros")

    # Test cases for the multiply function
    def test_multiply_positive_numbers(self):
        result = multiply(2, 3)
        self.assertEqual(result, 6, "Multiplying positive numbers")

    def test_multiply_negative_numbers(self):
        result = multiply(-1, 1)
        self.assertEqual(result, -1, "Multiplying negative numbers")

    def test_multiply_zeros(self):
        result = multiply(0, 5)
        self.assertEqual(result, 0, "Multiplying by zero")

    # Test cases for the divide function
    def test_divide_positive_numbers(self):
        result = divide(6, 2)
        self.assertEqual(result, 3, "Dividing positive numbers")

    def test_divide_by_zero(self):
        result = divide(5, 0)
        self.assertEqual(result, "Cannot divide by zero", "Dividing by zero")

if __name__ == '__main__':
    unittest.main()
