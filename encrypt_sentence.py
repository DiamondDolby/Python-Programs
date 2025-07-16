def encrypt_sentence(sentence):
    words = sentence.split()
    encrypted_words = []

    vowels = 'aeiouAEIOU'

    for i in range(len(words)):
        word = words[i]
        if (i + 1) % 2 != 0:  # Odd position (1-based index)
            encrypted_words.append(word[::-1])
        else:  # Even position
            consonants = ''.join([ch for ch in word if ch not in vowels])
            vowels_part = ''.join([ch for ch in word if ch in vowels])
            encrypted_words.append(consonants + vowels_part)

    return ' '.join(encrypted_words)

# Test the function
sentence = "the sun rises in the east"
encrypted_sentence = encrypt_sentence(sentence)
print(encrypted_sentence)
