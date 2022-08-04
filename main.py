import time

def sum_to_zero(my_list):
    '''
    Find two elements from my_list which sum to zero.
    Return a tuple of the two elements if they exist and None otherwise.
    '''
    for i1 in my_list:
        for j2 in my_list:
            if i1 + j2 == 0:
                return i1, j2
    return None


# Test Case 1
my_list = {4, 5, -7, -3, 8, -4}
start_time = time.time()
result = sum_to_zero(my_list)
end_time = time.time()
total_time = end_time - start_time
print("Input:", my_list)
print("Output:", sum_to_zero(my_list))
print("Time", total_time)

# Test Case 2
my_list = {5, -7, -3, 8, -4, 6, 0, -5, 10, -10, 7, 9, -7}
start_time = time.time()
result = sum_to_zero(my_list)
end_time = time.time()
total_time = end_time - start_time
print("\nInput:", my_list)
print("Output:", sum_to_zero(my_list))
print("Time", total_time)

# Test Case 3
my_list = {}
start_time = time.time()
result = sum_to_zero(my_list)
end_time = time.time()
total_time = end_time - start_time
print("\nInput:", my_list)
print("Output:", sum_to_zero(my_list))
print("Time", total_time)