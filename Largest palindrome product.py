def n_to_list(num):
    list = [int(i) for i in str(num)]

    return list


def is_palindrome(num):
    list = n_to_list(num)
    list_reversed = []

    for i in range(len(list) - 1, -1, -1):
        list_reversed.append(list[i])

    return list_reversed == list


largest_palindrome = 0


for i in range(100, 1000):
    for j in range(100, 1000):
        if is_palindrome(i * j) and i * j > largest_palindrome:
            largest_palindrome = i * j
else:
    print(largest_palindrome)
