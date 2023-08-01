def remove_all_after(list, border):

    try:
        index_of_border = list.index(border)  # find the index of the border 
        if border not in list:                  
            return list 
        return list[:index_of_border+1]   #start from 0 and remove element after the border
    
    except ValueError:
        return list 