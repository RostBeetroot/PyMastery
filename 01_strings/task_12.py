user_input = input('Enter a big string with a word "pig": ')

words = user_input.split()
censored_words = ['####' if word.lower() == 'pig' else word for word in words]

print(' '.join(censored_words))
