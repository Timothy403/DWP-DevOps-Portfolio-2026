def sum_positive(numbers_list):
    positive_total = 0

    for num in numbers_list:
        if num * -1 < 0:
            positive_total += num

    return positive_total


sum_positive([10, -1, -5, 20])
