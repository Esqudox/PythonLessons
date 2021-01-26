from abc import ABC, abstractmethod

class AbstractClothes(ABC):

    @abstractmethod

    def get_square(self):
        pass

class Clothes(AbstractClothes):

    def __init__(self, art, size, height):

        self.art = art
        self.size = int(size)
        self.height = int(height)

    @property

    def get_full_square(self):
        return f'Общая площадь ткани Артикул №{self.art} - {round((self.size / 6.5 + 0.5) + (self.height / 6.5 + 0.5))} '

class Coat(Clothes):

    def __init__(self, art, size, height):
        super().__init__(art, size, height)

    def get_square(self):
        return f'Ткань для пальто Артикул №{self.art} - {round(self.size / 6.5 + 0.5)}'

class Suit(Clothes):

    def __init__(self, art, size, height):
        super().__init__(art, size, height)

    def get_square(self):
        return f'Ткань для костюма Артикул №{self.art} - {round(self.height / 6.5 + 0.5)}'

coat_1 = Coat(12, 190, 48)
suit_1 = Suit(12, 190, 48)
print(coat_1.get_square())
print(suit_1.get_square())
print(coat_1.get_full_square)