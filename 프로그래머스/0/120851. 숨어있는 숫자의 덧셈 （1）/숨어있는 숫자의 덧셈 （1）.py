def solution(my_string):
    # 문자열에서 숫자만 추출
    numbers = [int(char) for char in my_string if char.isdigit()]
    return sum(numbers)
    
    '''
    def solution(my_string):
        numbers = []
        for char in my_string:
            if char.isdigit():
                numbers.append(int(char))
    return sum(numbers)
    '''
