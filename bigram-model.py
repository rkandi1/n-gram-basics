import queue as q


class Node:
    def __init__(self, next_word, probability):
        self.nword = next_word
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


def bigram_model(word_table, split_line):
    """
    Creates a bi-gram string model which can be used for autocomplete.

    :type word_table: dict
    """
    for i in range(1,len(split_line)):
        if split_line[i-1] not in word_table:
            word_table[split_line[i-1]] = q.PriorityQueue()
        word_table[split_line[i-1]].put(Node(word_table[split_line[i]], 1/len(word_table[split_line[i-1]])))



if __name__ == "__main__":
    word_table = dict()
    fw = open("edited_queries.txt", 'w')

    try:
        with open("cw09b-trec_eval-queries.txt", 'r') as f:
            # for line in f:
            line = f.readline()
            line = '<s> ' + line[:len(line)-1] + ' </s>\n'
            bigram_model(word_table, line.split(" "))
                # In case we need this same format again
                # fw.write(line)
    except IOError:
        print("Unable to write!")

    finally:
        fw.close()

    print(word_table)
