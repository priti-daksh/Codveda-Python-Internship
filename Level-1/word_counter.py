try:
    with open("sample.txt", "r") as file:
        content = file.read()

        words = content.split()
        word_count = len(words)

        print("File read successfully!")
        print("Total number of words:", word_count)

except FileNotFoundError:
    print("Error! File not found.")