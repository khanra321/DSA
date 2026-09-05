"""Bubble short"""

arr = [23,32,54,3,6,13,1]
l = len(arr)
for i in range(l-1):
    for j in range(l-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)
