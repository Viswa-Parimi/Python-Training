n=int(input("enter a number:"))
print("original number",n)
a=str(n)
rev_a=a[::-1]
if(a == rev_a):
    print("Yes. Given number is palindrome number")
else:
    print("No. Given number is not palindrome number")