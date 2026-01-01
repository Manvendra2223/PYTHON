
## Password Strength Checker 

password ="Secure3P@ss"

if len(password) < 8:
    print("Password is too short. It must be at least 8 characters long.")
elif len(password) > 20:
    print("Password is too long. It must be no more than 20 characters long.")

print("Password length is acceptable.")

