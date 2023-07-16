class Animal:
    def __init__(self):
        self.have_eyes = 2

    def breathe(self):
        print("Inhale, exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("We're doing this underwater.")

    def swim(self):
        print("I'm swimming")


my_fish = Fish()
my_fish.breathe()
