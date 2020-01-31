import os
import sys
import pandas
import argparse


class Parser:
    data: dict
    opt: dict
    file_name: str

    def __get_file(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-f", "--file", help="Enter the data file", type=str, default="data/data.csv")
        parser.add_argument("-p", action="store_true", help="Render the progression")
        parser.add_argument("-lr", "--learningrate", help="Render the progression", type=float, default=0.01)
        args = parser.parse_args()

        self.file_name = args.file
        self.opt = {"prog": args.p, "lr": args.learningrate}
        if os.path.splitext(self.file_name)[1] != ".csv":
            print("The file is in the wrong format, need a CSV file.")
            sys.exit(0)

    def __open_file(self):
        print(f"Reading file: {self.file_name}")
        self.file = pandas.read_csv(f"{os.path.abspath(self.file_name)}")

    def __get_data(self):
        self.__open_file()
        self.data['km'] = list(self.file['km'])
        self.data['price'] = list(self.file['price'])
        if not all(isinstance(e, int) for e in self.data['km']) or not all(
                isinstance(e, int) for e in self.data['price']):
            print("Not the same number of data for the 'km' and 'price' parameter or invalid number")
            sys.exit(0)

    def __init__(self):
        self.data = {}
        self.__get_file()
        self.__get_data()

    def return_dataset(self):
        return self.data, self.opt
