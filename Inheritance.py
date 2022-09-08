class Mammal:
    def walk (self):
        print("walk")


class Dog(Mammal):
    pass # pass this , dont worry about it


class Dog(Mammal):
    def bark (self):
        print("bark")


class Cat(Mammal):
    def be_annoing(self):
        print ("be annoing")


dog1 = Dog()
dog1.walk()

cat1 = Cat ()
cat1.be_annoing()