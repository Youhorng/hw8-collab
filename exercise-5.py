def reverse_ascending(numbers):
    result = []
    start = 0
    end = 0

    for i in range(len(numbers) - 1):
        if numbers[i] >= numbers[i + 1] and start != end:
            result.extend(numbers[end:start - 1:-1])
            start = end + 1
            end = i + 1
        if start != end:
            result.extend(numbers[end:start - 1:-1])
    return result

