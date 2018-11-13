import random
import string


def process_file(filename, skip_header):
    hist = {}
    fyle = open(filename)

    for line in fyle:
        for word in line.split():
            word = word.lower()
            hist[word] = hist.get(word,0) + 1

    return hist




def total_words(hist):
    return sum(hist.values())


def different_words(hist):
    i = 0
    for word in hist.items():
        i+= 1
    return i
    print(different_words(hist))

def most_common(hist):
    temp = []
    for word, frequency in hist.items():
        temp.append((frequency,word))
    temp.sort()
    temp.reverse()
    return temp



def print_most_common(hist, num=10):
    common_wordlist = most_common(hist)
    print (common_wordlist[:num])

def main():
    hist = process_file('blackbook.txt', skip_header=True)
    print('Total number of words:', total_words(hist))
    print('Average number of words per review:', total_words(hist)/25)
    print('Number of different words:', different_words(hist))

    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[0:50]:
        print(word, '\t', freq)

    words = process_file('words.txt', skip_header=False)


if __name__ == '__main__':
    main()
    pass