def count_duplicates(string):
    string_lower = string.lower()
    repeat_dict = {}
    count = 0
    for char in string_lower:
        if char not in repeat_dict:
            repeat_dict[char] = 1
        else:
            repeat_dict[char] += 1
    for value in repeat_dict:       
        if repeat_dict.get(value) > 1:     
            count += 1
    print(count)
    return count

