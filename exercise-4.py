def chunking_by(numbers, chunck):
    
    big_chunck= []

    num_of_chunck = len(numbers) // chunck

    # iterate over the numbers of chunck so as to divide each chunck
    for i in range(num_of_chunck): 

        start_index = i * chunck 
 
 
        end_index = start_index + chunck

        current_list = numbers[start_index:end_index]

        big_chunck.append(current_list)

    remaining_element = len(numbers) % chunck

    if remaining_element > 0:
        
        # get the numbers from the remaining element to the last element
        last_chunck = numbers[-remaining_element:] 
        big_chunck.append(last_chunck)
        

    return big_chunck
    

print(chunking_by([5, 4, 7, 3, 4, 5, 4], 3))

