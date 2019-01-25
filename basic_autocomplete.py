import bigram_model
import model_testing


def complete_query(query, individual_gram_count):
    sentence = query + " "
    # todo 1.1: Make a method change once we convert query to heap
    next_word = individual_gram_count[query][0].next
    while next_word != "</s>":
        sentence += next_word + ' '
        # todo 1.2: Make a method change once we convert query to heap
        next_word = individual_gram_count[next_word][0].next
    return sentence


# todo: Clean up the code, especially the uni-gram and bi-gram stuff
if __name__ == "__main__":
    unigram_count = dict()
    individual_gram_count = dict()

    with open('files/train_set.txt', 'r') as f:
        for line in f:
            _, line = line.split('.')
            line = "<s> " + line[:len(line) - 1] + " </s>"
            line_list = line.split(" ")
            bigram_model.bigram_counter(unigram_count, line_list)
            bigram_model.individual_word_counter(individual_gram_count, line_list)

        bigram_model.individual_probabilities(individual_gram_count, unigram_count)

    PP = model_testing.perplexity("files/test_set.txt", individual_gram_count)
    print(PP)

    # while True:
    #     query = str(input("Make a query: "))
    #     isahit = False
    #     query = query.split(' ')[0]
    #     for node in individual_gram_count["<s>"]:
    #         if node.next == query:
    #             sentence = complete_query(query, individual_gram_count)
    #             print(sentence)
    #             isahit = True
    #             break
    #
    #     if not isahit:
    #         print(query)
