class Car:
    def nove(self):
        print("Машина едет")

    def stop(self):
        print("Машина стоит")

    my_car = Car()
    my_car1 = Car()

    #my_car.move()
    #my_car.stop()

    #my_car1.move()
    #my_car1.stop()

    print(my_car)
    print(type(my.car))
    print(isinstance(my_car, Car))
    print(isinstance(my_car, object))
    print(my_car == my_car1)
    print(id(my_car), id(my_car1))

    #Атрибуты by.cor
    print(dir(my.car))
    print(my_car.__dict__)
    print(dir(input))