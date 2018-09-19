########################
#Course: CS23022
#Author: Cezar Barba
#Assignment: Lab 1 Option C(Password Cracking)
#Instructor: Diego Aguirre TA: Manoj Saha
#Date of Last Modification: 9/18/2018
#The purpose of this program is to generate a password that, when hashed while concatenated
#with its respective salt value, will compare the hashed value to a list of hashed passwords
#to see if it is the correct one.
########################
import hashlib

def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig

def main():
    #hex_dig = hash_with_sha256('This is how you hash a string with sha256')
    #print(hex_dig)
    
    pass_max_len=7
    pass_current_len=3
    
    
    with open("password_file.txt") as pass_file:
        for line in pass_file:
            #print(line)
            current=line.split(',')
            password_checker(pass_max_len,pass_current_len,current)
    
   
    #If you comment out lines 26-30 and uncomment these next four lines you can test other variables
    ###test = ["User0", "jjbgis", "e0ed8f4991bfbfd73fe604e7d29f77c39185aebe9fab828d4183941de71cf066"]#the password should be 2419445
    ###test1 = ["test", "test", "90e2cd6afaf9cdef6eb243188c6d09247658dfc06feb2ca784c67a4220bbd4e4"]#the password should be 1234
    ###password_checker(pass_max_len,pass_current_len,test)
    ###password_checker(pass_max_len,pass_current_len,test1)
    
    
    
def password_checker(pass_max_len,pass_current_len, current):
    
    #if the generated password is larger than 7 digits it exits the recursion
    if pass_current_len > pass_max_len:
        print("Unable to find a password for "+current[0])
        return
   
    zeros="0"#zeros that will be concatenated to passwd since integers can't be stored as 000
    passwd=0#password attempts will always start at zero
    
    
    while len(str(passwd)) <= pass_current_len:
        passwd_attempt = zeros* ((pass_current_len- len(str(passwd))))+str(passwd)+current[1]
        #print(passwd_attempt)#uncomment this to show the generated password that will be hashed
        if hash_with_sha256(passwd_attempt) == str(current[2]):#once a suitable password has been found the the recursion is exited
            print("The password for "+current[0]+ " is "+ str(passwd))
            return
 
        passwd+=1
    #When the while loop fails to find a suitable password of the current length it performs a recursive call to look for a password with a longer length   
    return password_checker(pass_max_len,pass_current_len+1,current)
    
   ####lines 67-73 were an unsucsessful attempt at recursion. It would start at "9999999" and make a recursive call if it is not the
   ####password. The next password attemt would be "9999998" and so on and so forth. This could not work since python has a limit
   ####of about 1000 recursions that it can perform. There is a way to increase the limit of recursions using sys.setrecursionlimit
   ####but it is still limited by what python can do. 
   # print(passwd)
    #if len(passwd) < pass_min_len:
     #   return
    #if hash_with_sha256(passwd+current_line[1]) == current_line[2]:
        #print("The password for " +current_line[0]+ " is: " +passwd)
        #return
    #return password_checker(pass_min_len, str(int(passwd)-1),current_line)
    
main()
    

    
    