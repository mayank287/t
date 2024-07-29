def find_max(data_list):
   
    if not data_list:
        raise ValueError("List cannot be empty")
    return max(data_list)

def find_min(data_list):

    if not data_list:
        raise ValueError("List cannot be empty")
    return min(data_list)

def calculate_sum(data_list):
 
    if not data_list:
        raise ValueError("List cannot be empty")
    return sum(data_list)

def compute_average(data_list):
  
    if not data_list:
        raise ValueError("List cannot be empty")
    return sum(data_list) / len(data_list)  

def find_median(data_list):

    if not data_list:
        raise ValueError("List cannot be empty")
    sorted_list = sorted(data_list) 
    mid_index = len(sorted_list) // 2
    if len(sorted_list) % 2 == 0:
        return (sorted_list[mid_index - 1] + sorted_list[mid_index]) / 2
    else:
        return sorted_list[mid_index]
