def solution(n):
    pieces = 7
    pizza = 1
    while n > pieces:
        n -= pieces
        pizza += 1
    return pizza