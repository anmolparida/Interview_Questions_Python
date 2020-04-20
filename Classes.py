
class Car(object):
    wheels = 4
    # used to initialize attributes of a object
    def __init__(self,make, model = '550i'):
        self.make = make # is same as self.makeOfCar = make
        self.model = model

    def info(self):

        print('make if the car: '+ self.make)
        print('model of the car: ' + self.model)


c1 = Car('BMW', '550i') # instance of the class is created
c1.info()
c2 = Car('AUDI', '550d')
c2.info()

print(Car.wheels)
print(c2.make)
print(c2.model)

wheels = 10
print(c2.wheels)
