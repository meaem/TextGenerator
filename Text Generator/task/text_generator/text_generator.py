import random


def load_corpus(file_name):
    f = open(file_name, 'r', encoding="utf-8")
    tokens = []
    for line in f:
        tokens.extend(line.split())
    return tokens


def get_bigrams(tokens):
    return list(zip(tokens[:-1], tokens[1:]))


def get_trigrams(tokens):
    return [(x + " " + y, z) for x, y, z in zip(tokens[:-2], tokens[1:-1], tokens[2:])]


def get_markov_dict(tokens):
    """
    :param tokens: list of head/tail tuples (bi-grams)
    :return: markov dict. A dictionary where keys are heads and
        each value is a dictionary of tails and their counts
    """
    result = {}
    for head, tail in tokens:
        t = result.setdefault(head, {tail: 0})  #
        t.setdefault(tail, 0)
        t[tail] += 1

    return result


def generate_random_sentence(markov_dict, max_length):
    words = []
    notfound = True
    while notfound:
        first_word = random.choice(list(markov_dict.keys()))
        notfound = False
        if first_word[0].isupper():
            for c in ['.', '!', '?']:
                if first_word.find(c) != -1:
                    notfound = True
                    break
        else:
            notfound = True

    words.extend(first_word.split())

    while len(words) <= max_length - 1:
        word = " ".join(words[-2:])
        next_list = list(markov_dict[word].keys())
        next_counts = list(markov_dict[word].values())

        word = random.choices(next_list, next_counts)[0]
        words.extend(word.split())

    while words[-1][-1] not in ['.', '!', '?']:
        word = " ".join(words[-2:])
        next_list = list(markov_dict[word].keys())
        next_counts = list(markov_dict[word].values())

        word = random.choices(next_list, next_counts)[0]
        for w in word.split():
            words.append(w)
            if w[-1] in ['.', '!', '?']:
                break

    return words


def main():
    corpus_file_name = input()
    tokens = load_corpus(corpus_file_name)
    grams = get_trigrams(tokens)
    markov_dict = get_markov_dict(grams)
    for _ in range(10):
        sent = generate_random_sentence(markov_dict, 5)
        print(" ".join(sent))

main()
