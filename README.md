This is a small script with Python 

this language is new for me , i learn the basic , function, variables,conditions <br>
I already did programmation but it's like to learn a new language
for example in English is "hello" and French is "Bonjour".
Flutter and Python are different but i'm really want to learn Python for to realize my dream to work in IT.

i don't want to lie , i have a cheat sheet of python with me to memorize.

## Why i did this exercice

<h2>first step for my final objectif with Python </h2>

i did this first version because , i want to play with back end server <br>
* Collect Information
* Store Information
* Securize Data

# How i did this script

for the V1 , i created pwd text for starting after that <br>
i created a condition while is true with a mode variable who print a question, following the answer of this variable mode, i created 3 options <br>
the first , if mode = q , the application quit, does mean , the user don't want to go further. <br>
the second, if mode = add, the user want to add a new password<br>
I created a function add() who ask the name and password <br>
For to Open a file when the information tapping, i just did the search on Google lol <br>
How to open a file in Python , a lot of informations but i was inspirated by this website <br>
https://www.geeksforgeeks.org/open-a-file-in-python/ <br>
Of course i copy the code and i adapted my code about what i need <br>
about the answer "name" and "password" , i had the idea the put a pipe for to separate , name and password. 

Code for V1 version (i will improve this code later)

# Code V1 

pwd = input ("click for Safety password following instruction")

def add():
    name = input ('Account name ')
    pwd= input ('Password ')

    with open("passwordFile.txt", "a") as a:
        a.write(name + "|" + pwd + "\n")

while True:
    mode = input(" new password or use the same password 'add' or 'q' ")
    if mode == "q":
        break
        
    elif mode == "add":
        add()   
    else:
        print('Invalid Password')

# End of V1

<h2>Don't forget , i'm just starting in python, i need to control the basic before to play an other level </h2>

# V2

I need to secure data , i read actually Fernet Documentation

# Final goal

I have two dream , the first work for a E commerce start up or a bank

create a database <br>
to collect customer information, for example <br>
* name
* surname
* age
* profession
* e-mail
* address
* bank details
  
 etc... but also secure the information collected and set up an internet banking payment interface.

 I really want to create a Ecommerce webSite ,not really for the design but for the paiement interface , like Stripe, learn , how i can optimize and use this.

 My second dream , if i validate the first condition to be a programmer , is to be a teacher , to learn peoples , how to code <br>
 but i have a lot of things to learn because i'm a beginner lol ^^ . <br>

 Wish me luck :)
