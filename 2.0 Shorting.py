"""Bubble short"""

# arr = [23,32,54,3,6,13,1]
# l = len(arr)
# for i in range(l-1):
#     for j in range(l-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
# print(arr)

"""Selection short"""
arr = [23,32,54,3,6,13,1]
l = len(arr)
for i in range(l-1):
    min = i
    for j in range(i+1, l):
        if arr[j] < arr[min]:
            min = j
        else: 
            continue
    arr[i], arr[min] = arr[min], arr[i]
print(arr)
        
