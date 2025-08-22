import sys


def binary_to_decimal(binary_str):
    if binary_str == "":
        return 0
    if binary_str[0] == '1':
        return 2 ** (len(binary_str) - 1) + binary_to_decimal(binary_str[1:])
    else:
        return 0 + binary_to_decimal(binary_str[1:])


def main(binary):
    print(binary_to_decimal(str(binary)))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else: 
        print("Please provide a binary string ")

    