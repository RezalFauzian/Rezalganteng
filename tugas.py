def check_input_types(input1, input2, input3):
    if isinstance(input1, str) and isinstance(input2, int) and isinstance(input3, float):
        return "Valid input types"
    else:
        return "Invalid input types"

# Test cases
print(check_input_types("Hello", 5, 3.14))  # Valid case
print(check_input_types("World", "5", 3.14))  # Invalid case: second input is not an integer
print(check_input_types(123, 5, 3.14))  # Invalid case: first input is not a string
print(check_input_types("Python", 5, "3.14"))  # Invalid case: third input is not a float
