def count_vowels(input_string):
    lowercase_string = input_string.lower()

    # count vowels
    count_a = lowercase_string.count('a')
    count_e = lowercase_string.count('e')
    count_i = lowercase_string.count('i')
    count_o = lowercase_string.count('o')
    count_u = lowercase_string.count('u')

    total_vowels = count_a + count_e + count_i + count_o + count_u
    return total_vowels


user_input = input("Enter a text: ")

vowels_count = count_vowels(user_input)

print(f"Number of vowels in the entered string: {vowels_count}")
