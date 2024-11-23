num1 = float(input(" Please Enter the First : "))
num2 = float(input(" Please Enter the Second : "))

a = num1
b = num2

if(num1 == 0):
    print("\n HCF of {0} and {1} = {2}".format(a, b, b))

while(num2 != 0):
    if(num1 > num2):
        num1 = num1 - num2
    else:
        num2 = num2 - num1

hcf = num1   
print("\n HCF of {0} and {1} = {2}".format(a, b, hcf))