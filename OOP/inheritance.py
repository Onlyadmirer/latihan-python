class animal:
    def __init__(self, isalive, isanimal):
        self.isalive = isalive
        self.isanimal = isanimal
    def dead(self):
        self.isalive = False
        return self.isalive

# cat = animal(True, True)
# print(cat.dead())

class cat(animal):
    def __init__(self, isalive, isanimal, color):
        super().__init__(isalive, isanimal)
        self.color = color

cat = cat(True, True, "white")
print(cat.dead())
print(cat.color)