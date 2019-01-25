from math import log2


def perplexity(test_file, gram_dict):
    with open(test_file) as f:
        log_probability_sum = 0
        N = 0
        for line in f:
            _, line = line.split('.')
            line = "<s> " + line + " </s>"
            split_line = line.split(" ")
            for i in range(1, len(split_line)):
                prob = next_probability(split_line[i-1], split_line[i], gram_dict)
                try:
                    log_prob = log2(prob) * -1
                except ValueError:
                    # print("Cannot take log of 0")
                    log_prob = 10
                log_probability_sum += log_prob
                N += 1
        print(log_probability_sum)
        return log_probability_sum * (1/N)


def next_probability(word, next_word, gram_dict):
    if word in gram_dict:
        # Todo: Change!!!
        for node in gram_dict[word]:
            if node.next == next_word:
                return node.probability

    # If no such values exist
    return 0
