def insertionSortRecursive(arr,n):
    # base case
    if n<=1:
        return
     
    # Sort first n-1 elements
    insertionSortRecursive(arr,n-1)
    #Insert last element at its correct position in sorted array.\'\'\'
    last = arr[n-1]
    
    j = n-2
     
      # Move elements of arr[0..i-1], that are
      # greater than key, to one position ahead
      # of their current position 
    while (j>=0 and arr[j]>last):
        arr[j+1] = arr[j]
        j = j-1
 
    arr[j+1]=last
    print('last:', last,'array:',arr)
     

 
# Main program to test insertion sort 
array = [12,11,13,5,6,8,14]
size = len(array)
print('Antes da ordenação : ', array)
insertionSortRecursive(array, size)
print('Depois da ordenação: ', array)

 
# Contributed by Harsh Valecha
