#     # 1. Array traversal: means visiting every element of an array one by one.
# arr = [10,20,30,40,50]
# for a in arr:
#     print(a,end=",")

#     # Traversla by index  Time Complexcity:---- O(n), because array seen one time.
# arr = [10,20,30,40,50]
# for b in range(len(arr)):
#     print(arr[b])

#     # Confusing in append 
# arr1 = [1,2,3]
# arr2 = arr1
# arr1.append(4)
# print(arr2)

#     # 2. Sum of all element
# arr = [1,2,3,4,5]
# sum = 0
# for i in arr:
#     sum += i
# print(sum)

#     # using sume function
# arr = [1,2,3,4,5]
# print(sum(arr))
    
#     # 3. Find max number 
# ar3 = [3,10,42,12,5]
# max = 0
# for i in ar3:
#     if max < i :
#         max = i
# print(max)

#     # 4. Searching 
# ar = int(input("Enter how many number you put:"))
# ar4 = []
# i = 1
# while ar>0:
#     arra=int(input(f"Enter {i} no : "))
#     ar4.append(arra)
#     ar-=1
#     i+=1
# tar = int(input("Enter what no you find : "))
# for i in range(len(ar4)):
#     if tar == ar4[i]:
#         print("find at index ", i)
#         break
# else:
#     print(f"{tar} is not found in this array.")
