# Program takes in Command Line Variable (CLV), proesses them in sysvariables
# and prints out a message incorperating CLV


#imports
import sys


def main():
    # getting first CLI stored in list object sys.argv at index 1 and 2
    print(f"Hello {sys.argv[1]} and {sys.argv[2]}.")
    print(f"Goodbye {sys.argv[1]} and {sys.argv[2]}.")


if __name__ == "__main__":
    main()
