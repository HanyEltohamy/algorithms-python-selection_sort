def selection_sort(arr):
    for i in range(len(arr)):
      minimumValueIndex=i
      for j in range(i+1,len(arr)):
        if(arr[j]<arr[minimumValueIndex]):
          minimumValueIndex=j
      (arr[i],arr[minimumValueIndex])=(arr[minimumValueIndex],arr[i])
      
      
data = [-2, 45, 0, 11, 3]
selection_sort(data)
print('Sorted Array in Ascending Order:')
print(data)