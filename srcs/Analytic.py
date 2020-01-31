import copy

from srcs.Graph import Graph


class Analytic(Graph):
    m: float
    b: float
    lr: float
    cost: float
    nb_data: int
    dataset: dict

    def __init__(self, dataset: dict, lr=0.001):
        self.lr = lr
        self.cost = 0
        self.dataset = dataset
        self._dataset = copy.deepcopy(dataset)
        self.nb_data = len(dataset['km'])

        self.b = 0
        self.m = 0
        self.mem = []
        self.standardisation()

        super().__init__(self._dataset['km'], self._dataset['price'], 0, 0, [])

    def standardisation(self):
        self.dataset['km'] = [x / max(self.dataset['km']) for x in self.dataset['km']]
        self.dataset['price'] = [x / max(self.dataset['price']) for x in self.dataset['price']]

    def estimate_price(self, km):
        return self.b + self.m * km

    def estimate_m(self):
        tmp_m = 0
        for i in range(self.nb_data):
            tmp_m += (self.estimate_price(self.dataset['km'][i]) - self.dataset['price'][i]) * self.dataset['km'][i]
        return self.m - (self.lr / self.nb_data) * tmp_m

    def estimate_b(self):
        tmp_b = 0
        for i in range(self.nb_data):
            tmp_b += self.estimate_price(self.dataset['km'][i]) - self.dataset['price'][i]
        return self.b - (self.lr / self.nb_data) * tmp_b

    def cost_function(self, tmp_cost: float):
        for i in range(self.nb_data):
            tmp_cost = tmp_cost + (self.estimate_price(self.dataset['km'][i]) - self.dataset['price'][i])
        return (1 / float(self.nb_data)) * tmp_cost

    def gradient_descent(self):
        print("Start calculating theta0 and theta1 with the gradient descent.")
        tmp_cost: float = -1
        while True:
            tmp0 = self.estimate_b()
            tmp1 = self.estimate_m()
            self.b = tmp0
            self.m = tmp1
            self.mem.append({'b': tmp0, 'm': tmp1})
            tmp_cost = self.cost_function(tmp_cost)
            if round(tmp_cost, 10) == round(self.cost, 10):
                break
            self.cost = tmp_cost
            tmp_cost = 0

        self.b = self.b * max(self._dataset['price'])
        self.m = (self.m * max(self._dataset['price'])) / max(self._dataset['km'])
        print("theta0 : {}\ntheta1 : {}".format(self.b, self.m))
