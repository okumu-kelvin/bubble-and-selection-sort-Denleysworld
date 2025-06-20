def bubble_sort(unsorted_list):
    for n in range(len(unsorted_list) - 1, 0, -1):
        for i in range(n):
            if unsorted_list[i] > unsorted_list[i + 1]:
                unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i + 1], unsorted_list[i]
    return unsorted_list
      
        
print(bubble_sort([4, 5, 3, 4]))  



