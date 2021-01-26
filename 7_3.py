class MyCell:

    def __init__(self, cell):
        self.cell = int(cell)

    def __str__(self):
        return f'Новая клетка - {self.cell * "*"}'

    def __add__(self, other):
        return MyCell(self.cell + other.cell)

    def __sub__(self, other):
        sub = self.cell - other.cell
        return MyCell(sub) if sub > 0 else print('Результат меньше нуля!')

    def __mul__(self, other):
        return MyCell(self.cell * other.cell)

    def __truediv__(self, other):
        return MyCell(self.cell // other.cell)

    def make_order(self, cells_in_row):
        result = ''
        for i in range(int(self.cell / cells_in_row)):
            result += f'{"*" * cells_in_row}\n'
        result += f'{"*" * (self.cell % cells_in_row)}'
        return result


cell_1 = MyCell(7)
cell_2 = MyCell(3)
cell_3 = MyCell(11)
cell_4 = cell_1 * cell_3

print(cell_1)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 / cell_2)
print(cell_4.make_order(7))
