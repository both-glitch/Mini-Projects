import sqlite3

conn = sqlite3.connect('c:/both/30day/resume/CRUDDTB.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS CRUDDTB(Name TEXT, Pass TEXT)''')

def Choosing():
    print("---------------")
    print("   1. Create")
    print("   2. Read")
    print("   3. Update")
    print("   4. Delete")
    print("   x. Exit")
    print("---------------")
def CheckNum(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid Characters, Try again")

def Create(amount):
    for i in range(amount):
        name = input("Enter Name: ")
        pw = input("Password: ")
        cur.execute('''INSERT INTO CRUDDTB (Name, Pass) VALUES (?, ?)''',(name, pw))
    conn.commit()
def Read(amount):
    if amount <= 0:
        print("Enter number greater than 0")
        return
    rows = cur.execute(f"SELECT Name, Pass FROM CRUDDTB LIMIT {amount}").fetchall()
    if not rows:
        print("No record found")
        return
    for row in rows:
        print(row[0],row[1])
def Update(oldname, newname, newpass):
    cur.execute('''UPDATE CRUDDTB SET Name = ?, Pass = ? WHERE Name = ?''', (newname, newpass, oldname, ))
    print(newname, newpass)
    conn.commit()
def Delete(delname):
    confirm = input(f"Are you sure you want to delete {delname} (y/n): ")
    if confirm.lower() == "y":
        cur.execute('''DELETE FROM CRUDDTB WHERE Name = ?''',(delname, ))
        conn.commit()
        print("Successfully Deleted")
    else:
        return

while True:
    Choosing()
    choose = input("Choose one: ")
    match choose:
        case "1":
            numcreate = CheckNum("Number to add: ")
            Create(numcreate)
        case "2":
            numread = CheckNum("How many to read: ")
            Read(numread)
        case "3":
            oldname = input("Old name: ")
            cur.execute('SELECT Name, Pass FROM CRUDDTB WHERE Name = ?', (oldname,))
            row = cur.fetchone()
            if row is None:
                    print("No name found, Add instead")
                    continue
            else:
                newname = input("New name: ")
                newpass = input("New password: ")
                Update(oldname, newname, newpass)

        case "4":
            delname = input("Name to delete: ")
            cur.execute('SELECT Name, Pass FROM CRUDDTB WHERE Name = ?', (delname,))
            row = cur.fetchone()
            if row is None:
                print("No name found")
                continue
            else:
                Delete(delname)
        case "x":
            print("Leaving...")
            conn.close()
            break
        case _: 
            print("Invalid choice, try again.")