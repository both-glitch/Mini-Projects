import re
while True:
    pw = input("Enter pw: ")
    if " " in pw:
        print("No Space")
        continue
    if len(pw) <= 5 or len(re.findall("[^a-zA-Z0-9]",pw))==0:
        print("Password should be longer than 5 and contain special character")
        continue
    if len(re.findall("[0-9]",pw))<1:
        print("Password should contain number")
        continue
    if len(re.findall("[a-z]",pw))<1:
        print("Password should contain alphabet")
        continue
    print("Strong Password")
    break
            
