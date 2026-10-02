n=int(input("Enter any 3 digit natural num: "))
thi=n%10
n=n//10
sec=n%10
n=n//10
fir=n%10
n=n//10
sum=fir+sec+thi
print("sum of all the digit: ",sum)
