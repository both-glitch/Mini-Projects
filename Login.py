import sqlite3
import re      

con = sqlite3.connect("Login.sqlite")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS Artist")

cur.execute("CREATE TABLE IF NOT EXISTS Account(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, User TEXT, Pass Text)")
def pw_strength():
    while True:
        st_pass = input("Password: ")
        if " " in st_pass:
            print("No Space")
            continue
        if len(st_pass) <= 5 or len(re.findall("[^a-zA-Z0-9]",st_pass))==0:
            print("Password should be longer than 5 and contain special character")
            continue
        if len(re.findall("[0-9]",st_pass))<1:
            print("Password should contain number")
            continue
        if len(re.findall("[a-z]",st_pass))<1:
            print("Password should contain alphabet")
            continue
        cf_pass = input("Confirm Password: ")
        if st_pass != cf_pass:
            print("Password do not match")
            continue
        break
    return cf_pass

def create(user):
    cur.execute("SELECT * FROM Account WHERE User = ?", (user,))
    row = cur.fetchone()
    if row is not None:
        print("User already exist")
        return False
<<<<<<< HEAD
    st_pass = pw_strength()
    cur.execute("INSERT INTO Account(User, Pass) VALUES(?,?)", (user, st_pass))
    print("Sucessfully Created")
    con.commit()
=======
    while True:
        st_pass = input("Password: ")
        cf_pass = input("Confirm Password: ")
        if st_pass != cf_pass:
            print("Password do not match")
            continue
        cur.execute("INSERT INTO Account(User, Pass) VALUES(?,?)", (user, st_pass))
        print("Sucessfully Created")
        con.commit()
        break
>>>>>>> 033072c4af4fd01d8b500b0076bd33deec746950
    return True

def login(user,st_pass):
    cur.execute("SELECT * FROM Account WHERE User=? ", (user,))
    row = cur.fetchone()
    if row is None:
        print("Incorrect Username or Password")
        return False
    if row[1] != user or row[2] != st_pass:
        print("Incorrect Username or Password")
        return False
    print("Loging Succesffully")
    return True

while True:
    choice = input("Choice (1. Create, 2. Login, x. Exit): ")
    match choice:
        case "1":
            while True:
                user = input("Username: ")
                if not create(user):
                    continue
                break
        case "2":
            while True:
                user = input("Username: ")
                st_pass = input("Password: ")
                if not login(user,st_pass):
                    continue
                break
        case "x":
            con.close()
            break
