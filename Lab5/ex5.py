class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def make_sound(self):
        pass

    def move(self):
        print(f"{self.name} is moving.")

class Mammal(Animal):
    def __init__(self, name, habitat, fur_color):
        super().__init__(name, habitat)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} makes a mammalian sound.")

    def give_birth(self):
        print(f"{self.name} is giving birth.")

class Bird(Animal):
    def __init__(self, name, habitat, wing_span):
        super().__init__(name, habitat)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} chirps like a bird.")

    def fly(self):
        print(f"{self.name} is flying with a wingspan of {self.wing_span} cm.")

class Fish(Animal):
    def __init__(self, name, habitat, scale_color):
        super().__init__(name, habitat)
        self.scale_color = scale_color

    def make_sound(self):
        print(f"{self.name} makes a bubbling sound.")

    def swim(self):
        print(f"{self.name} is swimming with {self.scale_color} scales.")


lion = Mammal(name="Lion", habitat="Savannah",  fur_color="Golden")
sparrow = Bird(name="Colibri", habitat="Forest", wing_span=2)
shark = Fish(name="Shark", habitat="Ocean", scale_color="Gray")

lion.make_sound()
lion.give_birth()
lion.move()
print()

sparrow.make_sound()
sparrow.fly()
sparrow.move()
print()

shark.make_sound()
shark.swim()
shark.move()