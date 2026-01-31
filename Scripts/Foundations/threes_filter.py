def get_threes(numbers):
    threes_list = []

    # Loop through the numbers
    for num in numbers:
        # Check if the number is divisible by 3
        if num % 3 == 0:
            threes_list.append(num)

    return threes_list
