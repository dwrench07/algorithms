arr = [10,3,4,1,9,2,5]
def mergeSort(arr):
  if(len(arr) == 1):
    return arr
  else:
    middle = int(len(arr)/2)
    left = []
    right = []
    i = 0
    j = int(middle)
    while i < middle:
      left.append(arr[i])
      i = i+1
    while j < len(arr):
      right.append(arr[j])
      j = j+1
    left=mergeSort(left)
    right=mergeSort(right)
    x=y=z=0
    while x < len(left) and y < len(right):
        if left[x]<=right[y]:
            arr[z] = left[x]
            z = z+1
            x = x+1
        else:
            arr[z] = right[y]
            z = z+1
            y = y+1
    while x < len(left):
        arr[z] = left[x]
        z = z+1
        x = x+1
    while y < len(right):
        arr[z] = right[y]
        y = y+1
        z = z+1
    return arr
        
            
print(mergeSort(arr))

