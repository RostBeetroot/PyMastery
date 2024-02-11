def replaсe_words(string):
    words = string.split()
    reversed_string = ' '.join(reversed(words))
    return reversed_string


assert replaсe_words("Hello, World") == "World Hello,"
assert replaсe_words("Hi, There.") == "There. Hi,"
assert replaсe_words("") == ""
