def solution(price):
    if 100000 <= price < 300000:
        return int(price*0.95)
    elif 300000 <= price < 500000:
        return int(price*0.9)
    elif price >= 500000:
        return int(price*0.80)
    else:
        return price   