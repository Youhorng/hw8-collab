def replace_last(numbers):
    if len(numbers) >= 1:
        last_element = numbers.pop()
        numbers.insert(0, last_element)
    return numbers 

y = replace_last([2,3,4,1])
print(y)
