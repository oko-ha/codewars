def balanced_parens(n):
    answer = []

    def backtracking(left, right):
        global parens
        if left > 0:
            if left < right:
                parens += ')'
                backtracking(left, right - 1)
                parens = parens[:-1]
            parens += '('
            backtracking(left - 1, right)
            parens = parens[:-1]
        else:
            parens += ')' * right
            answer.append(parens)
            parens = parens[:-right]

    global parens
    parens = ""
    backtracking(n, n)

    return answer