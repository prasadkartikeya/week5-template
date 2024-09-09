#Factorial coding by using function
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
n=int(input("enter the n values: "))
res=factorial(n)
print("factorial of ",n,"is",res)
















    