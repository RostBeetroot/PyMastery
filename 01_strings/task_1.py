car = input('Enter your favourite car: ')
output = f"Your favourite car is, {car}!"
print(output)

third_character = output[3]
print(f'№1 The third character is, {third_character}')

penultimate_character = output[-2]
print(f'№2 The penultimate character is, {penultimate_character}')

first_five_characters = output[0:5]
print(f'№3 The first five character is, {first_five_characters}')

except_last_two = output[:-2]
print(f'№4 The entire line except the last two characters is, {except_last_two}')

even_indexes_characters = output[::2]
print(f'№5 All characters with even indexes characters are, {even_indexes_characters}')

odd_indexes_characters = output[1::2]
print(f'№6 The odd indexes characters are, {odd_indexes_characters}')

characters_in_reverse_order = output[::-1]
print(f'№7 All characters in reverse order are, {characters_in_reverse_order}')

# one_after_another_in_reverse_order = [:1:-1]
# print(f'№8 All characters of the string one after another in reverse order, starting from the last one are, '
#       '{one_after_another_in_reverse_order}')

length_of_this_string = len(output)
print(f'The length of the string is {length_of_this_string}')
