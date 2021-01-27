class ComplexNum:

    def __init__(self, a, b):

        self.a = int(a)
        self.b = int(b)

    def __str__(self):
        return f'{self.a} + {self.b}i'

    def __add__(self, other):
        return f'{self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        return f'{self.a * other.a - self.b * other.b} + {self.a * other.b + self.b * other.a}i'

a = ComplexNum(1, 2)
b = ComplexNum(2, 7)
print(a)
print(b)
print(a + b)
print(a * b)