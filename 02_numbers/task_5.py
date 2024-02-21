def calculate_n_plus_nn_plus_nnn(n):
    nn = int(str(n) * 2)
    nnn = int(str(n) * 3)
    result = n + nn + nnn
    return result


n = int(input("Enter an integer n: "))
result = calculate_n_plus_nn_plus_nnn(n)
print("Result of expression n + nn + nnn :", result)
