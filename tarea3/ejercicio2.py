import sys

def decimal_to_binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    return decimal_to_binary(n//2) + str(n % 2)

#print(int(decimal_to_binary(1010)))  # Example usage, should return '1010'

def main(decimal):
    print(int(decimal_to_binary(decimal)))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else: 
        print("Please provide a decimal number")
