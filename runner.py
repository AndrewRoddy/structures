import sys
from tokenizer import tokenize

def main():

    # Checks if the correct number of command line argument exists
    if len(sys.argv) != 2:
        raise Exception(f"Needs two system arguments.\n1: The program name\n2: The input file\nGiven: {sys.argv}")
        return

    input_file = sys.argv[1] # Gets input file
    file = open(file=input_file, mode="r") # Opens the file
    text = file.read().strip() # Reads file and removes newlines
    file.close() # Closes the file

    tokenize(text)

if __name__ == "__main__":
    main()
