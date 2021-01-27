class Date:

    def __init__(self, data):

        self.data_list = str(data)

    @classmethod

    def unpack(cls, date):

        new_data = []

        for i in date.split():
            if i != "-":
                new_data.append(i)
        return int(new_data[0]), int(new_data[1]), int(new_data[2])

    @staticmethod

    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2000 <= year <= 2090:
                    return 'Date is ok'
                else:
                    return 'Wrong year'
            else:
                return 'Wrong month'
        else:
            return 'Wrong day'

day_1 = Date('27 - 01 - 2021')
print(day_1.unpack('27 - 01 - 2021'))
print(Date.valid(27, 1, 2020))
print(Date.valid(18, 13, 2001))
print(Date.valid(34, 2, 2023))