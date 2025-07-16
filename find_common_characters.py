def find_common_characters(msg1, msg2):
    # Remove spaces
    msg1 = msg1.replace(" ", "")
    msg2 = msg2.replace(" ", "")

    result = []
    for char in msg1:
        if char in msg2 and char not in result:
            result.append(char)

    if not result:
        return -1
    else:
        return ''.join(result)

# Test the function
msg1 = "I like Python"
msg2 = "Java is a very popular language"
common_characters = find_common_characters(msg1, msg2)
print(common_characters)
