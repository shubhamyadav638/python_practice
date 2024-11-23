ch = input("Enter any character : ")[0]
if ch.isupper() :
    print("\n" + ch, "is uppercase:")
elif ch.islower() :
    print("\n" + ch, "is lowercase:")
else :
    print("\n" + ch, "is not an alphabet.")