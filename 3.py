def merging_Dict(*args):
   

    merged_dict = {}
    for d in args:
        merged_dict.update(d)
    return merged_dict

def common_keys(*args):
   

    if not args:
        return set()
    common_keys = set(args[0].keys())
    for d in args[1:]:
        common_keys = common_keys.intersection(set(d.keys()))
    return common_keys

def invert_dict(d):
    
    inverted_dict = {}
    for key, value in d.items():
        if value in inverted_dict:
            inverted_dict[value].append(key)
        else:
            inverted_dict[value] = [key]
    return inverted_dict

def common_key_value_pairs(*args):
    

    if not args:
        return []
    common_pairs = [(k, v) for k, v in args[0].items() if all(k in d and d[k] == v for d in args[1:])]
    return common_pairs


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 3, 'd': 4}
dict3 = {'c': 3, 'd': 4, 'e': 5}

print(merging_Dict(dict1, dict2, dict3))  
print(common_keys(dict1, dict2, dict3)) 
print(invert_dict({'a': 1, 'b': 2, 'c': 1}))  
print(common_key_value_pairs(dict1, dict2, dict3))  
