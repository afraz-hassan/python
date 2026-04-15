import re
import math

def passStrength():
    global password
    passwordTest = len(password) * math.log2(95)
    if (passwordTest <= 50):
        print("Password Strength: Weak")
    elif(passwordTest <= 85):
        print("Password Strength: Midium")
    elif(passwordTest <= 100):
        print("Password Strength: Strong")
    else:
        print("Password Strength: Very Strong")

capital = re.compile(r"[A-Z]{1,}")
small = re.compile(r"[a-z]{1,}")
digits = re.compile(r"[0-9]{1,}")
symbols = re.compile(r"[^a-zA-Z0-9]{1,}")
nospace = re.compile(r"\s")

print("\n\n\nA strong password is at least 12–16 characters long, combining uppercase/lowercase letters, numbers, and symbols." )
print("\nPlease Enter Strong Password: ", end="")

password = input()
password = password.strip()

capitalCheck = capital.findall(password)
smallCheck = small.findall(password)
digitsCheck = digits.findall(password)
symbolsCheck = symbols.findall(password)
nospaceCheck = nospace.findall(password)

passwordTest = len(password) * math.log2(95)


if len(password) < 12 or capitalCheck == [] or smallCheck == [] or digitsCheck == [] or symbolsCheck == [] or nospaceCheck:
    print("\nNot a Strong Password")
    if nospaceCheck:
        print("Please Do not add spaces between the Password")
    else:
        passStrength()
else:
    print("\nStrong Password")
    passStrength()