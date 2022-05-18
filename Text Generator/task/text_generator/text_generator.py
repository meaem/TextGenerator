from nltk.tokenize import word_tokenize


def load_corpus(file_name):
    f = open(file_name, 'r', encoding="utf-8")
    tokens = []
    for line in f:
        tokens.extend(line.split())
        # print("+")
    # tokens = word_tokenize(f.read().lower())
    # print(tokens[:100])
    return tokens


def get_bigrams(tokens):
    return list(zip(tokens[:-1], tokens[1:]))


def get_markov_dict(tokens):
    """
    :param tokens: list of head/tail tuples (bi-grams)
    :return: markov dict. A dictionary where keys are heads and
        each value is a dictionary of tails and their counts
    """
    result = {}
    for head, tail in tokens:
        t = result.setdefault(head, {tail: 0})#
        t.setdefault(tail, 0)
        t[tail] += 1

    return result


def main():
    corpus_file_name = input()
    tokens = load_corpus(corpus_file_name)
    bigrams = get_bigrams(tokens)
    # print(f"Number of bigrams: {len(bigrams)}")
    markov_dict = get_markov_dict(bigrams)
    while True:
        # print("**")
        user_input = input()

        if user_input == "exit":
            break
        try:
            head = user_input
            # print(f"**{head}**")
            selected = markov_dict[head]
            print(f"Head: {head}")
            for k in selected:
                print(f"Tail: {k}     Count: {selected[k]}")
        except TypeError:
            print("Type Error. Please input an integer.")
        except ValueError:
            print("Value Error. Please input an integer.")
        except IndexError:
            print("IndexError: list index out of range")
        except KeyError:
            print("Key Error. The requested word is not in the model. Please input another word.")


main()