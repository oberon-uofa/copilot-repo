import sys
code = __import__(sys.argv[1])

def main():
    for x in range(1, 10):
        print(code.triangle2(x))

main()
