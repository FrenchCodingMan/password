pwd = input ("click for Safety password following instruction")

def view():
    pass

def add():
    name = input ('Account name ')
    pwd= input ('Password ')

    with open("passwordFile.txt", "a") as a:
        a.write(name + "|" + pwd + "\n")

while True:
    mode = input(" new password or use the same password 'add' or 'q' ")
    if mode == "q":
        break
        
    elif mode == "view":
        view()
    elif mode == "add":
        add()   
    else:
        print('Invalid Password')
