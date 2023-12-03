class User:
    # class variable
    message = "This is User"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(self.message)

    def show_user(self):
        print("User ", self.name, " is aged ", self.age)

# inherit User class
# hence can access parent variable
class FacebookUser(User):
    #class variable
    my_message = "Facebook user!"

    def __init__(self, name, age):
        super().__init__(name, age)

    def show_info(self):
        print(self.my_message)

facebook_user = FacebookUser("Daniel", 25)
# child can access parent variable
print(facebook_user.message)
# child function overrides parent
facebook_user.show_info()

