# Python program to display the Fibonacci sequence


def test_fibo(n):
  if(n<=1):
    return n
  else:
    return (test_fibo(n-1) + test_fibo(n-2))

num= int(input("enter the number of which you want fibonacci sequence : "))
if(num <0):
  print("you have entered negative number ")

else:
  for i in range(num):
    print(test_fibo(i))

