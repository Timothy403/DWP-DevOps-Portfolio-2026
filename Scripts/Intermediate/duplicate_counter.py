def count_duplicates(string):
    string = string.lower()
    repeat_dict = {}
    count = 0
    for char in string:
      repeat_dict[char] = repeat_dict.get(char, 0) + 1
      duplicates_total = 0
    for key in repeat_dict.values():
      if key > 1:
      count += 1
return count

