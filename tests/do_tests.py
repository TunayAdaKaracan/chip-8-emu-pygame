import importlib
from os import listdir


def instruction_tests():
    for file in list(filter(lambda f: f[:4] and f[-3:] == ".py", listdir("./instructions"))):
        importlib.import_module("instructions."+file[:-3])
        print(f"{file[:-3]} test passed.")


if __name__ == "__main__":
    instruction_tests()