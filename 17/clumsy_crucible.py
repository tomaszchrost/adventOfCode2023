from data_parser import DataParser


class ClumsyCrucible:
    def __init__(self, data):
        self.data = data


def main():
    data = DataParser("data.dat")
    clumsy_crucible = ClumsyCrucible(data)
    print("x")


if __name__ == "__main__":
    main()
