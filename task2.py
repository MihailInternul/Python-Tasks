# Given a list of integers. Remove duplicates from the list and create a tuple. Find the minimum and maximum number.

def find_min_max(numbers):
    unique_numbers = tuple(set(numbers))

    min_value = min(unique_numbers)
    max_value = max(unique_numbers)

    return min_value, max_value


def remove_duplicates(numbers):
    unique_numbers = list(set(numbers))
    return unique_numbers


input_numbers = [5, 8, 9, 8, 4, 5, 3, 1, 1, 7, 4, 8]
min_value, max_value = find_min_max(input_numbers)
unique_numbers = remove_duplicates(input_numbers)

print(f"Original List: {input_numbers}")
print(f"Unique Numbers: {unique_numbers}")
print(f"Minimum Value: {min_value}")
print(f"Maximum Value: {max_value}")
