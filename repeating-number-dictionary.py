#Find the first repeating element in an array of integers

arr = []

print("please enter the elements (0 to stop):")
      
while True:
    element = int(input())
    if element != 0:
        arr.append(element)
    else:
        break
    
repeated_list = []

#bubble sort
n = len(arr)
for i in range(n):          
    for j in range(0, n-i-1):                    
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

#main
for num in arr:
    if num not in repeated_list:
        repeated_list.append(num)
    else:
        print("The first repeated element is: ", num)
        break





#2nd approach:
            
#arr = [6, 10, 5, 4, 9, 120, 4, 6, 10]

#counter = {}  

#for num in arr:
#    if num in counter:
#        counter[num] += 1
#        if counter[num] == 2:
#            print("The first repeating element is:", num)
#            break
#    else:
#        counter[num] = 1

#print(counter)
