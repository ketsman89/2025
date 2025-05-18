a = 500
name = input("enter your name: ")
def check_user(fun):
    
    def decor(*args, **kwargs):
        
        if args[0] != "admin":
            return "acess denied"
        
        value = fun(*args, **kwargs)
        return value
    return decor

@check_user
def balance(name):
    print(a)
    
print(balance(name))