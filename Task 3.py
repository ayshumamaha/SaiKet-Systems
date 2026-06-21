# Word Count Tool

from collections import Counter

file_name = "Sample.txt"

try:
    with open(file_name, "r") as file:
        content = file.read()

    lines = content.splitlines()
    words = content.split()
    characters = len(content)

    print("\n===== FILE ANALYSIS =====")
    print(f"Total Lines      : {len(lines)}")
    print(f"Total Words      : {len(words)}")
    print(f"Total Characters : {characters}")

    frequency = Counter(words)

    print("\nMost Common Words:\n")

    for word, count in frequency.most_common(10):
        print(f"{word} : {count}")

except FileNotFoundError:
    print("Error: File not found.")

except Exception as error:
    print("An unexpected error occurred:", error)
    
    
    
    
    
