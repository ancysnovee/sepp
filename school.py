import random
class student:
    def __init__(self,email,password,retype):
        self.email=email
        self.password=password
        self.retype=retype
        self.email_ids=[]
        self.register_id=[]
        
    def account_creation(self,email,password,retype):
        char=['@','#','*','$']
        if email[-10:]=="@gmail.com":
            if len(password)>=8:
                for i in self.password:
                    if i in char:
                        self.email_ids.append(email)
                        
                        return True

                return "passowrd should contain special symbols"
            else:
                return "password should contain min 8 char"
        else:
            return "invalid email id"
        
    def sign_in(self,email,password):
        if self.account_creation(self.email,self.password,self.retype):
            if self.email==email and self.password==password and email in self.email_ids:
                return "sign_in successful"
            else:
                return "user does not exists"
    def random(self):
        return random.randint(100000,999999)
        
    def unique_id(self):
        rg=self.random()
        if rg not in self.register_id:
            self.register_id.append(rg)
            return f"{rg} is your register id"
        else:
            self.unique_id()
            
                
        
        
if __name__=="__main__":
    i=student("ancysnovee@gmail.com","aa@aaaaaaa","aa@aaaaaaa")
    print(i.sign_in("ancysnovee@gmail.com","aa@aaaaaaa"))
    print(i.sign_in("anovee@gmail.com","aa@aaaaaaa"))
    print(i.unique_id())
    
    
