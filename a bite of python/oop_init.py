class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello! My name is', self.name)

Person('Swaroop').say_hi()
Person('Allahahah').say_hi()