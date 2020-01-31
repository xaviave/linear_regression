from srcs.Parser import Parser
from srcs.Analytic import Analytic
from srcs.FileHandler import FileHandler


if __name__ == "__main__":
    dataset, opt = Parser().return_dataset()
    a = Analytic(dataset, opt["lr"])
    a.gradient_descent()
    a.render(opt['prog'])
    FileHandler.create_file(a.m, a.b)
