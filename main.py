
def main():

    file = open(file="example.txt", mode="r") # Opens the file
    text = file.read().strip() # Reads file and removes newlines
    file.close() # Closes the file

    for char in text:
        print(char + "|")


if __name__ == "__main__":
    main()
