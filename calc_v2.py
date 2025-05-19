users = {1:{"name": "Papa", "height": 188, "weight": 88},
         2:{"name": "Mama", "height": 160, "weight": 55}, 
         3:{"name": "Son", "height": 140, "weight": 50}}

menu = """
Hello! It's your BMI dict! Can I help you?
Enter your choose
Show all users: L
Show user's info: R
Update user's info: U
Delete some user: D
Add new user: C
"""

def all_users(users):
    for k in users.values():
        print(k["name"])

def user_info(users):
    login = int(input("enter login: "))
    print(users[login])
    bmi = round(users[login]["weight"]/((users[login]["height"]/100)**2))

    print(bmi)
    n = (bmi - 20)//5
    m = 6 - n
    print("20" + "="*n + "I" + "="*m + "50")

def update_user():
    pass

def add_user(users):
    new_login = int(input("enter new login: "))
    new_name = input("enter name: ")
    new_height = int(input("enter new height: "))
    new_weight = int(input("enter new weight: "))
    users[new_login] = {"name": new_name, 
                        "height": new_height, 
                        "weight": new_weight}
    
def delete_user(users):
    login_to_delete = int(input("what login you want to delete? "))
    del(users[login_to_delete])
    

    
