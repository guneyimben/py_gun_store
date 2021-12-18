class User: 
    
    def __init__(self, username, password, login):
        self.username = username
        self.password = password
        self.login = login
        

    def Login(self):    
        user1 = User("admin", "1", True)
        user2 = User("admin2", "1", False)
        database = [user1,user2]
        
        successfulLogin = 0
        for item in database:
            if self.username == item.username:        
                if self.username == item.username and self.password == item.password: 
                    if item.login == False:
                        print("\n          Yasaklandınız!\n")
                        os.system("pause")
                        os.system("cls")
                        sys.exit()
                    else:
                        successfulLogin += 1
                    
        if successfulLogin == 0:
            print("\n          Kullanıcı Adı / Şifre hatalı!\n")
            return False

        else:
            return True