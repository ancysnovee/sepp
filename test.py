from school import student
def testing():
    t=student("ancysnovee@gmail.com","aa@aaaaaaa","aa@aaaaaaa")
    assert(t.sign_in("ancysnovee@gmail.com","aa@aaaaaaa"))== "sign_in successful"
    assert(t.sign_in("anovee@gmail.com","aa@aaaaaaa"))=="user does not exists"
    
if __name__=="__main__":
    testing()
    print("passed")