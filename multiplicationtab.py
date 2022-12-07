from re import I


n = int(input("Enter the number : "))
print("Multiplication table of",n)
for i in range(1, 11):
    mul = n*i 
    print(n,"*",i,"=",mul)