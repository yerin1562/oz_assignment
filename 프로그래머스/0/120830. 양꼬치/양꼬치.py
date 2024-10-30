def solution(n, k):
    np = 12000
    kp = 2000
    service = n//10
    newk = k-service
    answer = n*np + newk*kp 
    return answer
    # if n//10 >= 1:
    #     return n*np+k*kp-(n//10*2000)
    
