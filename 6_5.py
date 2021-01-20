class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Drawing')

class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Drawing with pen')


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Drawing with pencil')


class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Drawing with handle')

pen_1 = Pen('Blue')
pen_1.draw()

pencil_2 = Pencil('Gray')
pencil_2.draw()

handle_3 = Handle('Black')
handle_3.draw()
