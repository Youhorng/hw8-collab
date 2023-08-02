def reverse_ascending(numbers):
    result = []
    subsequence = []

    for i in range(len(numbers)):
        if i == 0 or numbers[i] > numbers[i-1]:
            subsequence.append(numbers[i])
        else:
            result.extend(subsequence[::-1])
            subsequence = [numbers[i]]

    result.extend(subsequence[::-1])

    return result

list = [5, 7, 10, 4, 2, 7, 8, 1, 3]
result = reverse_ascending(list)
print(result)