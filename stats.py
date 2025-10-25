def wordcount(text):
    first = text.split()

    return first

def lettercount(text):
    low = text.lower()
    letters = list(low)
    dictionary = dict()
    for i in letters:
        dictionary[i] = dictionary.get(i,0)+1
    return dictionary


