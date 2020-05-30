import sys
from pip._internal import main as pip_main

def wheel(package):
    pip_main(['wheel', package])

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            try:
                wheel(line)
            except Exception as e:
                print(e)
