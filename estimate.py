import re
import argparse


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("km", help="Kilometer of a car", type=int)
    args = parser.parse_args()
    return args.km


def open_file():
    try:
        with open('data/theta_saver.lr', 'r') as lr:
            file = lr.read()
            m = re.search(r'^theta0 : (?P<theta0>(-)?\d+\.\d+)\ntheta1 : (?P<theta1>(-)?\d+\.\d+)$', file)
        return float(m.group('theta0')), float(m.group('theta1'))
    except Exception:
        print("Error with the file.")
        exit(0)


def run():
    km = args()
    theta0, theta1 = open_file()
    print(f"The estimate price of the car is: {theta0 + (theta1 * km)}")


if __name__ == "__main__":
    run()
