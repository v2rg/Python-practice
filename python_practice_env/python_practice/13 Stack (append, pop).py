class User:
    def __init__(self):
        self.stack = []

    def first_in(self, new_value):
        self.stack.append(new_value)

    def last_out(self):
        return self.stack.pop()


user_0 = User()
print(user_0.stack)
user_0.first_in('new value')
user_0.first_in('new value 2')
user_0.first_in('new value 3')
print(user_0.stack)

print(user_0.last_out())
print(user_0.last_out())

print(user_0.stack)
