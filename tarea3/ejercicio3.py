import sys
def division_iterativa(a,b):
    if a == 0:
        return 0
    return 1 + division_iterativa(a - b, b)

def main(a, b):
    print(int(division_iterativa(a, b)))

if __name__ == "__main__":
    if len(sys.argv) > 2:
        main(int(sys.argv[1]), int(sys.argv[2]))
    else: 
        print("Please provide two numbers")
