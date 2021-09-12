print("Python program to find the sum of first n positive integers")
a=int(input("Enter the first term:"))
an=int(input("Enter the last term:"))
d=int(input("Enter the common difference:"))
n=an-a+1
sn=n*(2*a+(n-1)*d)/2
print("Sum=",sn)


