class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self._income = {'wage': wage, 'bonus': bonus}
        self.name = name
        self.surname = surname
        self.position = position

class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

worker_1 = Position('Pavel', 'Durov', 'mechtatel', 20000, 10000)

print(worker_1.get_full_name())
print(worker_1.get_total_income())