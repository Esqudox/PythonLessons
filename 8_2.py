class MyErr:

    def __init__(self, div, den):

        self.div = int(div)
        self.den = int(den)


    def zero_division(self, div, den):
        try:
            return div / den
        except:
            return 'На ноль делить нельзя!'

a = MyErr(2, 0)
b = MyErr(3, 1)
c = MyErr(4, 0)
d = MyErr(5, 2)

print(a.zero_division(2, 0))
print(b.zero_division(3, 1))
print(c.zero_division(4, 0))
print(d.zero_division(5, 2))