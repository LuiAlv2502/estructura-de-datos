
import sys

def count_characters(a, c):
    count = 0
    if a == "":
        return 0
    if a[0] == c:
        count += 1
    return count + count_characters(a[1:], c)
  # Output: 8

def main(a):
    print(count_characters(a, 'a'))

if __name__ == "__main__":
    if len(sys.argv) > 2:
        main(sys.argv[1], sys.argv[2])
    else: 
        print("Please provide a string and a character")