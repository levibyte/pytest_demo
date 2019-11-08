from myapp.lib import MAX_ITEMS, get_first_name, Car, open_car


def get_max_items():
    return MAX_ITEMS


def get_full_name(arg):
    return ' '.join((get_first_name(arg), 'Bar'))

def hopar():
    return "aaa"+hopar2("xxx","yyy")

def hopar2(arg1,arg2):
    return arg1+arg2

def get_car_make(make=None):
    car = Car()
    if make:
        car = Car.for_make(make)
    return car.get_make()


def get_car_wheels():
    return Car().wheels


def get_roll_call():
    return Car.roll_call()


def close_car(car):
    states = []
    with open_car(car) as car:
        states.append(car.closed)
    states.append(car.closed)
    return states


class Major(object):
    def __init__ (self,a,b):
        self.a = a
        self.b = b

    def get_a(self,y):
        return y+int(self.get_b(y))
        
    def get_b(self,x):
        return int(x+b)
        
