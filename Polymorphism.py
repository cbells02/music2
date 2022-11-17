class Dog():

    def __init__(self,name):
        self.name = name


    def speak(self):
        return self.name +" says woof"


class Cat():

    def __init__(self,name):
        self.name = name


    def speak(self):
        return self.name +" says meow"


niko = Dog("niko")
felix = Cat("Felix")

print(niko.speak())
print(felix.speak())


