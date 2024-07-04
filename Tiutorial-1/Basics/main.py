print("Hello world")

#mathematical operation
# print(15+10)
# print(15*10)
# print(15/10)
# print(15**10)
# print(15%10)
# print(15//10)

#variables 
# x=15
# y=10
# print(x+y)

# x=10+115
# y=100+12
# print(x**y)

x=input("Player 1:  ")
y=input("Player 2:  ")
if x=="stone" and y=="paper":
    print("Player 2 wins......")
elif x=="paper" and y=="stone":
    print("Player 1 wins.....")
elif x=="paper" and y=="paper":
    print("Draw")
elif x=="stone" and y=="stone":
    print("Draw")

