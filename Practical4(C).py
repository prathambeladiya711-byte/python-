def find_max_min(numbers):
    maximum = max(numbers)
    minimum = min(numbers)
    return maximum, minimum

nums = [12, 45, 7, 89, 23, 56]

max_value, min_value = find_max_min(nums)

print("Maximum value:", max_value)
print("Minimum value:", min_value)