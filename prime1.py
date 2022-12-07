n = int(input("Enter the number : "))
if(n<=1):
    print("Please enter number greater than 1")
else:
    for i in range(2, n+1):
        if(n%i!=0):
            print(n,"is Prime number")
            break
        else:
            print(n,"is not Prime number")
            break
