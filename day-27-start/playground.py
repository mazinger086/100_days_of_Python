# Unlimited arguments
def add(*args):
    result = 0
    for n in args:
        result += n
    return result




def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs['add'] # 2 + 3 = 5
    n *= kwargs['multiply'] # 5 * 5 = 25
    print(n)



calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Sentra")
print(my_car.model)