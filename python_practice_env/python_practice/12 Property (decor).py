class User:
    def __init__(self):
        self.__username = 'first'

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, new_username):
        self.__username = new_username


user_0 = User()
print(user_0.username)
user_0.username = 'second'
print(user_0.username)
