import os
import sys
import argparse


class Parser:
    data: list
    file_name: str

    def __get_file(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-f", "--file", help="Enter the data file", type=str)
        args = parser.parse_args()
        self.file_name = args.file if args.file else "data/data.csv"
        if os.path.splitext(self.file_name)[1] != ".csv":
            print("The file is in the wrong format, need a CSV file.")
            sys.exit(0)

    def __open_file(self) -> str:
        print(f"Reading file: {self.file_name}")
        with open(f"{os.path.abspath(self.file_name)}", "r") as fd:
            file = fd.read()
        return file

    def __get_data(self):
        tmp_data = self.__open_file().split()
        tmp_data.pop(0)
        for line in tmp_data:
            tmp = line.split(',')
            self.data.append([int(tmp[0]), int(tmp[1])])

    def __init__(self):
        self.data = []
        self.__get_file()
        self.__get_data()
        print(self.data)
        print(max(self.data, key=lambda x: x[0]), min(self.data, key=lambda x: x[0]))
        print(max(self.data, key=lambda x: x[1]), min(self.data, key=lambda x: x[1]))
