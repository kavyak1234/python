def find_second_largest(numbers):
    if len(numbers)<2:
        return "list must contain least two numbers"
    unique_numbers=sorted(list(set(numbers)),reverse=True)
    if len(unique_numbers)<2:
        return "list must contain least two distinct numbers"
    return unique_numbers[1]

