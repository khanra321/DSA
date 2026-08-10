#   # 1. veriable: Veriable is a container that contain data(int, float, char, Bool)

# age =23
# name ="Akash"
# Hight =5.4
# print(" name: ",name,"\n","age: ",age,"\n","hight: ",Hight)


#   # 2. Input(alwaya taken as string thats why need type custing) and Output(we use print())
# n = input("Enter a value: ")
# print(n)
# print(type(n))

    # for type custing we use "int()", "chr()", "folat()".
# p = int(input("Enter a number: "))
# print(p, type(p))

#   #Use Map()
# x,y = map(int,input("EnterTwoValueBySpace:").split())
# print(f"{x} + {y} = {x+y}")

#     # 3. if-else: if-else is used for decision making.

# age = int(input("Enter your age:"))

# if age < 18:
#     print("You are minor")
# else: 
#     print("you are adult.")

    # if-elif-else
marks = int(input("Enter marks:"))

if 90<marks<=100:
    print("O")
elif 80<marks<=90:
    print("E")
elif 70<marks<=80:
    print("A")
elif 60<marks<=70:
    print("B")
elif 50<marks<=60:
    print("c")
elif 40<marks<=50:
    print("D")
else:
    print("F, Faild!...!")
