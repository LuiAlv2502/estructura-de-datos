import sys
def invert_int(n):
    if n == 0:
        return 0
    return int(str(n % 10) + str(invert_int(n // 10))) if n >= 10 else n

def main(a):
    print(invert_int(a))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else: 
        print("Please provide a number")
