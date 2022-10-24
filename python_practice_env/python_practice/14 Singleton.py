class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, first, second):
        self.first = first
        self.second = second


inst_0 = Singleton('1', '1')
inst_1 = Singleton('22', '22')
inst_2 = Singleton('333', '333')

print(inst_0.first, inst_0.second)
print(inst_1.first, inst_0.second)
print(inst_2.first, inst_0.second)
