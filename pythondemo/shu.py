
def gcd(x, y):
    if y == 0:
        return x
        return gcd(y, x%y)
        x=250
        y=475
        print("gcd of", x, "and", y,"is:",)