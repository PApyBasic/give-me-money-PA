#Do not CopyRight
#PA

print("Choose with a Number")
print("-------------------------")
print("Do you have money?")
print("1-Yes")
print("2-No")
A = int(input())
if A==2:
    print("-------------------------")
    print("Get out")
    exit()
if A==1:
    print("-------------------------")
    print("How much do you have?")
    print("example:10000")
B = int(input())
if B>50000:
    print("-------------------------")
    print("6219 8618 7736 2060")
    print("Can you give me some money?")
    print("1-Yes")
    print("2-NO")
if B<50000:
    print("-------------------------")
    print("Get out")
    exit()
C = int(input()) 
if C==1:
    print("-------------------------")
    print("Thank you😊")
if C==2:
    print("-------------------------")
    print("Get out🤬")