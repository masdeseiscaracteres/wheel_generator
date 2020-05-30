import sys
from subprocess import check_call, CalledProcessError

def build_wheel(package):
    try:
        check_call(["python", '-m', 'pip', 'wheel', '--no-deps', package])
    except CalledProcessError as e:
        print(e)
        
if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            build_wheel(line)
            
