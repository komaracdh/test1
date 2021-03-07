from data import *
#import data

def sign_up():
    while True:
        koricnickoIme = input('Enter your username: ')
        koricnickaLozinka = input('Enter your password: ')
        if koricnickoIme in users:
            h = users.index(koricnickoIme)
        else:
            print('Invalid data,try again')
            sign_up()
        if koricnickaLozinka == passwords[h]:
            print('You have successfully logged in', role[h])
            #izbrisati ovo posle
            mainwindow()
        
def mainwindow():
    nesto = True
    while nesto == True:
        print("Welcome to hotel")
        print("1.Sign up")
        print("2.Register")
        print("3.Exit") 

        option = input("Choose option: ")
        
        if option == "1":
            sign_up()
        elif option == "2":
    # register()
            print("?")
        elif option =="3":
            print("Goodbye")  
        else:
            print("Wrong option")



mainwindow()

 





      
   