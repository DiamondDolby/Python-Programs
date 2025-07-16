def find_correct(word_dict):
    correct = 0
    almost_correct = 0
    wrong = 0

    for correct_word, given_word in word_dict.items():
        if correct_word == given_word:
            correct += 1
        elif len(correct_word) == len(given_word):
            mismatch_count = 0
            for c1, c2 in zip(correct_word, given_word):
                if c1 != c2:
                    mismatch_count += 1
            if mismatch_count <= 2:
                almost_correct += 1
            else:
                wrong += 1
        else:
            wrong += 1

    return [correct, almost_correct, wrong]
