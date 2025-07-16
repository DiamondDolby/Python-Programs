def encode(message):
    if not message:
        return ""

    encoded = ""
    count = 1

    for i in range(1, len(message)):
        if message[i] == message[i - 1]:
            count += 1
        else:
            encoded += str(count) + message[i - 1]
            count = 1

    # Append the last group
    encoded += str(count) + message[-1]
    return encoded

# Test cases
encoded_message = encode("ABBBBCCCCCCCCAB")
print(encoded_message)  # Output: 1A4B8C1A1B

# More tests
print(encode("AAAABBBBCCCCCCCC"))  # 4A4B8C
print(encode("AABCCA"))            # 2A1B2C1A
print(encode(""))                  # Empty string input => ""
print(encode("XYZ"))               # 1X1Y1Z
