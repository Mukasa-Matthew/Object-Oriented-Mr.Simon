class Car:
    def __init__(self, speed, color):
        print(speed)
        print(color)

#store the values in the object
        self.speed = speed
        self.color = color

#show that the constructor was called
        print("the init is called")



ford = Car(200, "red")
audi = Car(250, "blue")
toyota = Car(150, "green")

print(ford.speed)
print(audi.speed)
print(toyota.speed)