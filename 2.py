def add_element(set1, element):
   
    set1.add(element)

def remove_element(set1, element):
    
    if element in set1:
        set1.remove(element)

def union(set1, set2):

    return set1 | set2

def intersection(set1, set2):
   
    return set1 & set2

def difference(set1, set2):
   
    return set1 - set2

def is_subset(set1, set2):
  
    return set1.issubset(set2)

def set_length(set1):
 
    count = 0
    for _ in set1:
        count += 1
    return count

def symmetric_difference(set1, set2):
 
    return set1 ^ set2

def power_set(set1):

    power_set = [set()]
    for element in set1:
        new_subsets = [subset | {element} for subset in power_set]
        power_set.extend(new_subsets)
    return power_set

def unique_subsets(set1):

    return power_set(set1)

# Example usage
set1 = {1, 2, 3}
set2 = {2, 3, 4}

add_element(set1, 4)
print(set1)  

remove_element(set1, 3)  
print(set1)
print(union(set1, set2)) 
print(intersection(set1, set2))  
print(difference(set1, set2)) 
print(is_subset({1, 2}, set1))
print(set_length(set1)) 
print(symmetric_difference(set1, set2)) 
print(power_set({1, 2}))  
print(unique_subsets({1, 2}))  
