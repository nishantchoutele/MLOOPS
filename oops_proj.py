class chatbook:
    __user_id = 0 
    def __init__(self):
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        self.__name = "default user"
        self.user_id = 0
        self.user_id += 1
        self.username = '' 
        self.password = '' 
        self.loggedin = False
        #self.menu()
    @staticmethod
    def get_id():
        return chatbook.__user_id
    @staticmethod
    def set_id(val):
        chatbook.__user_id = val 


    def get_name(self):                                                         
        return self.__name
    
    def set_name(self, value):
        self.__name = value
        
    


    def menu(self):
        user_input = input("""Welcome to chatbook !! How would u like to proceed?
                            1. Press 1 to signup
                            2. Press 2 to signin
                            3. Press 3 to write a post 
                            4. Press 4 to message a friend
                            5. Press any other key to exit
                           
                           ->""")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg
        else:
            exit()


    def  signup(self):
        email = input("Enter your email here -> ")
        password = input("Enter your password her ->")
        self.username = email
        self.password = password
        print("you  have signed up successfully !!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username=='' and self.password=='':
            print("Please sign up first by pressing 1 in the main menu")
        else:
            uname = input("enter your email/username here -> ")
            password= input("Enter your password here ->")
            if self.username==uname and self.password==password:
                print("You have signed in successfully !!")
                self.loggedin=True
            else:
                print("Please input the correct credentials..")
            print("\n")
            self.menu()

    def my_post(self):
        if self.loggedin==True:
            txt = input("Enter your message here ->")
            print (f"Following content has been posted ->{txt}")
        else:
            print("You need to sign in first to post something...") 
        print("\n")
        self.menu()   

    def sendmsg(self):
        if self.loggedin==True:
            txt = input("Enter your message here -> ")
            friend = input("Whom to send the message ")
            print(f"Your message has been send to {friend}")
        else:
            print("You need to sign in first to post something...")
        print("\n")
        self.menu()

user1 = chatbook()
            