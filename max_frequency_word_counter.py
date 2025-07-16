def max_frequency_word_counter(data):
    word = ""
    frequency = 0

    # Normalize the text
    words = data.lower().split()

    # Dictionary to count frequency
    freq_dict = {}
    for w in words:
        freq_dict[w] = freq_dict.get(w, 0) + 1

    # Find the word with highest frequency and max length if tied
    max_freq = 0
    max_word = ""
    for w, f in freq_dict.items():
        if f > max_freq or (f == max_freq and len(w) > len(max_word)):
            max_freq = f
            max_word = w

    word = max_word
    frequency = max_freq

    # Output (per requirement)
    print(word, frequency)
