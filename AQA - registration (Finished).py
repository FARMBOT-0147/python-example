####################################################################################################################

##                            declares all of the variables and functions                                           #

userTries = 0
userTries = int(userTries)

userNames=["user1","user2","user3","user4","user5"]
passWords=["pass1","pass2","pass3","pass4","pass5"]

check = "your Username or Password is incorrect "

def newUser ():
    newUsername = input ("Please enter new username: ")
    newPassword = input ("Please enter a new password: ")
    if newUsername in userNames:
        print ("Username or Password is already in use")
        return "NO"
    else:
        return "OK"

def checkUser():
    userName = input("Enter your Username: ")
    passWord = input("Enter your Password: ")
    for i in range (len(userName)):
        if userName == userNames[i]:
            if passWord == passWords[i]:
                return "OK"
            
####################################################################################################################

#                     prints the opening scene for the AQA registration program                                    #     

print ("#############################")
print ("#Welcome to AQA registration#")
print ("#############################")
print ("")
optionSelect = input("""Please select an operation to perform;
Type '1' : Register as a new user 
Type '2' : Sign in 
Type '3' : Exit 
Enter option here: """)
####################################################################################################################

#                                        option select                                                             #

if optionSelect == "1":
    result = newUser()
    if result == "OK":
        print ("""##############################################
#Welcome to AQA, user succsessfully logged in#
##############################################""")
    
elif optionSelect == "2":
    result = checkUser()
    print ("""##############################################
#Welcome to AQA, user succsessfully logged in#
##############################################""")

elif optionSelect == "3":
    print ("Shutting down")
    exit

else:
    print ("Valid option not selected, shutting down!")
    exit

####################################################################################################################
