# class animal:
#     name = ""
#     def eat(self):
#         print("i can eat")

# class dog:
#     def display(self):
#         print("my name is", self.name)

# labrador = dog()

# labrador.name = "rohu"
# labrador.eat()
# labrador.display()

# class shape:
#     def __init__(self, color):
#         self.color = color

# class rectangle(shape):
#     def __init__(self, color, width, height):
#         super().__init__(color)
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

# rect = rectangle("red", 5, 10)
# print(f"are of rectangle {rect.area()}")

# class circle(shape):
#     pi = 3.14
#     def __init__(self, color, jari):
#         super().__init__(color)
#         self.jari = jari

#     def luas(self):
#         return self.pi * self.jari**2

# area = circle("blue", 10)
# print(f"luas circle adalah: {area.luas()}")


class mammal:
    def mammal_info(self):
        print("mammal can give direct")

class wingedAnimal:
    def winged_animal_info(self):
        print("winged animal can flap")

class bat(mammal,  wingedAnimal):
    pass

b1 = bat()
b1.mammal_info()
b1.winged_animal_info()
