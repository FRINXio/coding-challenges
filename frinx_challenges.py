def capital_indices(word):
    indices = []
    all_capital = word.upper()
    for i in range(len(word)):
        if word[i] == all_capital[i]:
            indices.append(i)
    return indices


def recursive_palindrome(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    else:
        return recursive_palindrome(word[1:-1])


def transposition(matrix): return[[matrix[col][row] for col in range(len(matrix[0]))] for row in range(len(matrix))]


if __name__ == "__main__":
    print(capital_indices("PYthOn"))

    potential_palindromes = ["tenet", "redder", "frinx", "python"]
    for item in potential_palindromes:
        print(recursive_palindrome(item))

    print(transposition([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
