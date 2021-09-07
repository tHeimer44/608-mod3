def maximum(value1, value2, value3):
    """Return the maximum of three values."""
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value

value1 = input("Enter Max Value1 ")

value2 = input("Enter Max Value2 ")

value3 = input("Enter Max Value3 ")

min_input = input("Enter Minimum numbers separated by a space ").split()

min_list = list(map(int, min_input))

print ("Max of 3 number:", maximum(value1, value2, value3))
print ("Min number:", min(min_list))
