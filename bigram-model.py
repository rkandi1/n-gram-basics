import queue as q

class Node:
    def __init__(self, next_word, probability):
        self.next = next_word
        self.probability = probability

    def __le__(self, other):
        return self.probability <= other.probability

    def __lt__(self, other):
        return self.probability < other.probability

    def __gt__(self, other):
        return self.probability > other.probability

    def __ge__(self, other):
        return self.probability >= other.probability

    def __eq__(self, other):
        return self.probability == other.probability

    def get_word(self):
        return self.next


def bigram_counter(gram_count, split_line):
    for i in range(1,len(split_line)):
        curr_word = split_line[i-1]
        if curr_word not in gram_count:
            gram_count[curr_word] = 0
        gram_count[curr_word] += 1




if __name__ == "__main__":
    unigram_count = dict()

    with open('cw09b-trec_eval-queries.txt', 'r') as f:
        i = 0
        for line in f:
            line = "<s> " + line[:len(line)-1] + " </s>"
            bigram_counter(unigram_count, line.split(" "))
            if i == 2:
                break
            i+=1

    print(unigram_count)
