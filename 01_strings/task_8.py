def greet(name, owner):
    name = input("What is your name? ")
    owner = input("What is your owner's name? ")
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"


assert greet('Daniel', 'Daniel') == 'Hello boss'
assert greet('Greg', 'Daniel') == 'Hello guest'
