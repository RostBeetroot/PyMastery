def remove_h(input_text):
    first_h = input_text.find('h')
    last_h = input_text.rfind('h')

    if first_h != -1 and last_h != -1:
        input_text = input_text[:first_h] + input_text[last_h + 1:]
        return input_text
    else:
        return input_text


input_text = input('Enter random letters with h: ')
print(remove_h(input_text))
