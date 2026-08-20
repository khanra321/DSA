    # Recurtion: When a function call it self.
def num(n):
    if n == 0:      # Bass cass
        return 0
    print(n)        # First print  # Output: 5 4 3 2 1
    num(n-1)        # Recurtion call
num(5)              # Call function


    # Recurtion call first then print
    