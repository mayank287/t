import module_ListFunction as mlf


numbers = [x for x in range(1, 11)]
mixed_data = [5, "hello", 3.14, True]
empty_list = []


try:
    print("Maximum of", numbers, ":", mlf.find_max(numbers))
    print("Minimum of", numbers, ":", mlf.find_min(numbers))
    print("Sum of", numbers, ":", mlf.calculate_sum(numbers))
    print("Average of", numbers, ":", mlf.compute_average(numbers))
    print("Median of", numbers, ":", mlf.find_median(numbers))
except ValueError as e:
    print(e)

try:
    print("Maximum of", mixed_data, ":", mlf.find_max(mixed_data)) 
except ValueError as e:
    print(e, "- Function only works with numerical data")


try:
    mlf.find_max(empty_list)  
except ValueError as e:
    print(e)
