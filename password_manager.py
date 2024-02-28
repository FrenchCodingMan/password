from cryptography.fernet import Fernet

pwd = input ("click for Safety password following instruction ")

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()        

def view():
    with open("passwordFile.txt", "r") as a:
        for line in a.readline():
            data = line.rstrip()
            user,passW = data.split("|")
            print("User:", user, ",| Password", passW)

def add():
    name = input ('Account name ')
    pwd= input ('Password ')

    with open("passwordFile.txt", "a") as a:
        a.write(name + "|" + pwd + "\n")

while True:
    mode = input(" new password or use the same  'add' or 'q' ")
    if mode == "q":
        break
        
    elif mode == "view":
        view()
    elif mode == "add":
        add()   
    else:
        print('Invalid Password')
