import time, re

def create(numcreate):
    for i in range(numcreate):
        while True:
            namecreates = input("Name: ").strip().capitalize()
            if not namecreates:
                print("Input is Empty")
                continue
            if namecreates in name:
                print("Name Already in List")
                continue
            name.append(namecreates)
            break
    print("Sucesfully Added")
    
def read(numread):
    numreads = int(numread)
    if numreads>len(name):
        print(f"{numreads} is out of range, capped at {len(name)}")
        numreads = len(name)
    for i in range(numreads):
        print(f"{i+1}.",name[i])

def update(nameupdate):
    found = False
    for i in range(len(name)):
        if nameupdate == name[i]:
            while True:
                newname = input("New Name: ").strip().capitalize()
                if not newname or newname in name:
                    print("Name cannot be empty or repeated")
                    continue
                name[i] = newname
                print(f"Succesfully Updated, {nameupdate} -> {newname}")
                found = True
                break
            break
    if not found:
        print(f"{nameupdate}, not found in list")

def delete(namedelete):
    try:
        name.remove(namedelete)
        print("Sucessfully Delete")
    except ValueError:
        print(f"{namedelete}, not found in list")

def checkerror():
    if not name:
        print("Enter Name First")
        return True
    return False
        
def choosing():
    print("---------------")
    print("   1. Create")
    print("   2. Read")
    print("   3. Update")
    print("   4. Delete")
    print("   x. Exit")
    print(f"Total of {len(name)} names")
    print("---------------")


def showname():
    for i in range(len(name)):
        print(f"{i+1}.",name[i])

name = list()
while True:
    choosing()
    choice = input("Choosing: ")
    match choice:
        case "1":
            while True:
                numcreate = input("How many to create ( - to return ): ").strip()
                if numcreate == "-":
                    break
                if not numcreate:
                    print("Choice cannot be empty")
                    continue
                if re.findall("[a-z]",numcreate) or re.findall("[^a-zA-Z0-9]",numcreate):
                    print("Only Number")
                    continue
                if int(numcreate)<1:
                    print("Number Should be higher than 0")
                    continue
                else:
                    create(int(numcreate))
                    break
        case "2":
            if checkerror():
                continue
            while True:
                numread = input("How many to read ( - to return ): ").strip()
                if numread == "-":
                    break
                if not numread:
                    print("Choice cannot be empty")
                    continue
                if re.findall("[^0-9]",numread):
                    print("Only Number")
                    continue
                if int(numread)<1:
                    print("Number Should be higher than 0")
                    continue
                else:
                    read(numread)
                    break
        case "3":
            if checkerror():
                continue
            showname()
            while True:
                nameupdate = input("Name to update ( - to return ): ").strip()
                if nameupdate == "-":
                    break
                if not nameupdate:
                    print("Name cannot be empty")
                    continue
                update(nameupdate.strip().capitalize())
                break
        case "4":
            if checkerror():
                continue
            showname()
            while True:
                namedelete = input("Name to delete ( - to return ): ").strip().capitalize()
                if namedelete == "-":
                    break
                if not namedelete:
                    print("Name cannot be empty")
                    continue
                if namedelete not in name:
                    print("Name doesn't exist")
                    continue
                while True:
                    confirmation = input("Are you sure you want to delete (y/n): ")
                    match confirmation:
                        case "y":
                            delete(namedelete)
                            break
                        case "n":
                            print("Cancelled")
                            break
                        case _:
                            print("Choose only y or n")
                            continue
                break

        case "x":
            print("Exiting...")
            time.sleep(0.5)
            break