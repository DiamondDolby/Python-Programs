def sms_encoding(data):
    vowels = 'aeiouAEIOU'
    words = data.split()
    result = []

    for word in words:
        # Check if all characters are vowels
        if all(char in vowels for char in word):
            result.append(word)
        else:
            # Keep only consonants
            consonants = ''.join([char for char in word if char not in vowels])
            result.append(consonants)

    return ' '.join(result)
