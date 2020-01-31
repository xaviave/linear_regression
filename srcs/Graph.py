from matplotlib import pyplot


class Graph:
    x: list
    y: list
    m: float
    b: float
    mem: list

    def __init__(self, x, y, m, b, mem):
        self.x = x
        self.y = y
        self.m = m
        self.b = b
        self.mem = mem

    @staticmethod
    def aff_point(km, price):
        pyplot.plot(km, price, "+r")
        pyplot.ylabel('price')
        pyplot.xlabel('km')

    def aff_function(self):
        self.aff_point(self.x, self.y)
        pyplot.plot([(self.b + self.m * x) for x in range(max(self.x))], "b", linewidth=3)
        pyplot.show()

    def aff_progression(self):
        self.aff_point(self.x, self.y)
        scale = int(len(self.mem) / 20)
        for i in range(len(self.mem)):
            if i % scale == 0:
                pyplot.plot([(self.mem[i]['b'] * max(self.y)) + (self.mem[i]['m'] * max(self.y)) / max(self.x) * km for km in range(max(self.x))], "g", linewidth=3)

    def render(self, prog):
        self.aff_function()
        if prog:
            self.aff_progression()
        pyplot.show()
