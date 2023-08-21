def print_upper_words(words, must_start_with):
    """prints every word in list uppercased"""

    must_start_tuple = tuple(must_start_with)

    for word in words:
        lowered_word = word.lower()

        if lowered_word.startswith(must_start_tuple):
            print(word.upper())
