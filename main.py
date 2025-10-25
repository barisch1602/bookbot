import sys
from stats import wordcount
from stats import lettercount
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return(file_contents)


try:
    test = sys.argv[1]

    def main():
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        text = get_book_text(sys.argv[1])
        words = wordcount(text)
        wordcounts = len(words)

        print(f"Found {wordcounts} total words")
        print("--------- Character Count -------")


        sorted_values = sorted(lettercount(text).items(),reverse=True, key= lambda x:x[1])
        for i in range(len(sorted_values)):
            if sorted_values[i][0].isalpha() == True:
                print(f"{sorted_values[i][0]}: {sorted_values[i][1]}")

        print("============= END ===============")

    main()
except:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)