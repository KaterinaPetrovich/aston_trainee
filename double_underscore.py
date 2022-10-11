class Employee:

    def __new__(cls, *args, **kwargs):
        print("I am constructor")
        instance = super().__new__(cls)
        return instance

    def __init__(self, name, salary):
        print("I am initializer")
        self.name = name
        self.salary = salary

    def __getattribute__(self, item):
        if item == "lastname":
            return "no information"
        else:
            return super().__getattribute__(self, item)

    def __del__(self):
        print("destructor was called")

    def __repr__(self):
        return f"Employee({self.name}, {self.salary})"

    def __str__(self):
        return f"{self.name} with salary {self.salary}"

    def __add__(self, other):
        return self.salary + other.salary

    def __len__(self):
        return len(self.name)

    def __mul__(self, other):
        return self.salary * other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary


emp1 = Employee("max", 70000)
print(emp1.lastname)


# emp2 = Employee("kate", 80000)
#
# print(emp1 > emp2)

class Ten:
    def __get__(self, obj, objtype=None):
        return 10


class A:
    x = 5
    t = Ten()


a = A()
print(a.x)
print(a.t)


class Counter:

    def __init__(self, start, stop):
        self.start = start - 1
        self.stop = stop

    def __next__(self):
        self.start += 1
        if self.start <= self.stop:
            return self.start
        # raise StopIteration

    def __iter__(self):
        return self


c = Counter(1, 5)


# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))

class Item:

    def __init__(self, items):
        self.items = items

    def __getitem__(self, item):
        return self.items[item]


# i = Item(["1", "2", "3"])
# print(i[1])


class ContextManager:
    def __enter__(self):
        print("into context manager")
        return

    def __exit__(self, *args):
        print("out")


# with ContextManager():
#     print("smth")

class Mul:
    # def __init__(self):
    def __call__(self, a, b):
        return a * b


m = Mul()
print(m(3, 2))


class Temp:
    description = 'class for temperature manipulation'

    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def kelvin(self):
        return self.celsius + 273.15

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

    @classmethod
    def change_description(cls, new):
        cls.description = new


t = Temp(15)

print(t.kelvin_to_celsius(459))

Temp.change_description("bebebe")
print(t.description)