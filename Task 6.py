file_name = "Sample.txt"

try:

    file = open(file_name, "r")

    content = file.read()

    file.close()

    lines = content.splitlines()

    words = content.split()

    characters = len(content)

    print("\n===== FILE ANALYSIS =====")

    print("Total Lines:", len(lines))

    print("Total Words:", len(words))

    print("Total Characters:", characters)

except FileNotFoundError:
    print("File not found.")
    
    
