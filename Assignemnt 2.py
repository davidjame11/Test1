#string assignment DAVID JAMES J

print("user inputs")
Name=input("Enter your Name:")
Age=input("Enter your age:")
Favorite_Color=input("Enter your Favorite Color:")
print("")
print("")
output= "Hello,my name is {0}.I am {1} years old.My Favourite color is {2}"
print ("output:")
X= Name.strip().lower().split()
print(output.format(X[0],Age.strip(),Favorite_Color.strip().upper()))