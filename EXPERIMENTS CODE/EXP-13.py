def alphabeta(depth, alpha, beta, maximizing):
    if depth == 3:
        return 10

    if maximizing:
        value = alphabeta(depth + 1, alpha, beta, False)
        alpha = max(alpha, value)
        return value
    else:
        value = alphabeta(depth + 1, alpha, beta, True)
        beta = min(beta, value)
        return value

print("Best Score:", alphabeta(0, -999, 999, True))
