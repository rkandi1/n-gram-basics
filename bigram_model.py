
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

    def __str__(self):
        return self.next


def bigram_counter(gram_count, split_line):
    for index in range(1,len(split_line)):
        curr_word = split_line[index-1]
        if curr_word not in gram_count:
            gram_count[curr_word] = 0
        gram_count[curr_word] += 1


# Combine this method and the bigram_counter
def individual_word_counter(individual_gram_count, split_line):
    for index in range(1, len(split_line)):
        curr_word = split_line[index-1]
        if curr_word not in individual_gram_count:
            individual_gram_count[curr_word] = []
            individual_gram_count[curr_word].append(Node(split_line[index], 1))
            continue

        # This is inefficient. Rewrite it!!!
        for node in individual_gram_count[curr_word]:
            if node.__str__() == split_line[index]:
                node.probability +=1
                continue

        individual_gram_count[curr_word].append(Node(split_line[index], 1))


def individual_probabilities(individual_prob_count, unigram_count):
    for key in individual_prob_count.keys():
        for node in individual_prob_count[key]:
            node.probability = node.probability/unigram_count[key]
