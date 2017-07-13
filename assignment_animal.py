class Animal(object):
    def __init__(self,name):
        self.name=name
        self.health=100
        return

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print "Animal: {}, health: {}".format(self.name,self.health)
        return self

class Dog(Animal):
    #def __init__(self,name,health):
    def __init__(self,name):
        super(Dog,self).__init__(name)
        self.name = name
        self.health = 150
        return

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self,name):
        super(Dragon,self).__init__(name)
        self.name = name
        self.health = 170
        return

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        print "This is a dragon!"
        super(Dragon,self).displayHealth()
        return self

myAnimal = Animal("Donny").walk().walk().walk().run().run().displayHealth()
myDog = Dog("Keith").walk().walk().walk().run().run().pet().displayHealth()
myDragon = Dragon("Bobby").walk().walk().walk().run().run().fly().fly().displayHealth()
