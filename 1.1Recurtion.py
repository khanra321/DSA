#     # Recurtion: When a function call it self.
# def num(n):
#     if n == 0:      # Bass cass
#         return 0
#     print(n)        # First print  # Output: 5 4 3 2 1
#     num(n-1)        # Recurtion call
# num(5)              # Call function


#     # Recurtion call first then print
# def num(n):
#     if n == 0:
#         return
#     num(n-1)
#     print(n)  # Output : 1 2 3 4 5
# num(5)  

    # Factorial 
def fact(n):
    if n == 0:
        return 1
    count = n*fact(n-1)
    return count
c = int(input("Enter a number to find factorial: "))
print(fact(c))