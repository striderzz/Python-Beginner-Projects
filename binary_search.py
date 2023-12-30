def binary_search(list,element):
  
  start = 0
  end = len(list)
  middle = 0 
  steps = 0

  while start <= end:

    print(f'start: {start}, middle: {middle}, end:{end}, steps:{steps+1}')

    steps = steps + 1
    middle = (start + end)//2

    if element == list[middle]:
      print(f'{element} found at index {middle}')
      break

    elif element < list[middle]:
      end = middle - 1

    elif element > list[middle]:
      start = middle + 1
  return -1      
      

mylist = [1,2,3,4,5,6,7,8,9]
binary_search(mylist,4)       



