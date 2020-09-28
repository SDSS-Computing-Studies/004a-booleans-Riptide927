#! python3

#  Have the user enter a username 
# If the username is not "admin" then tell them it is an "invalid user", 
# but if it is, then ask them for a password 
# If they get the password correct (password is 12345password) 
# then display the message "Access granted"
# 1 marks

a = input("what is your user name\n")
if "admin" in a:
    b = input("what is your password\n")
    if "12345password" in b:
        print("acess granted")
else:
    print("Invalid user")