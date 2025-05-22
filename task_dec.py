# a = 500
# name = input("enter your name: ")
# def check_user(fun):
    
#     def decor(*args, **kwargs):
        
#         if args[0] != "admin":
#             return "acess denied"
        
#         value = fun(*args, **kwargs)
#         return value
#     return decor

# @check_user
# def balance(name):
#     print(a)
    
# print(balance(name))

login = input("Enter your login :")

def check_login(fun):
    def wrap_decor(*args, **kwargs):
        if login == "admin":
            value = fun(*args, **kwargs)
            return value
        else:
            print("access denied")
    return wrap_decor

@check_login
def balance():
    print("your balance is 5$")
    
balance()