def solution(brown, yellow):
    
    # 가로 x, 세로 y, x >= y
    # brown = 2*x + 2*(y-2) --> x+y = 1/2(brown +4)
    # yellow = x*y - brown --> xy = brown + yellow
    # yellow >= 1 --> x,y >=  3
    
    import math
    
    answer = []
    
    hap = math.floor((brown + 4) / 2)
    gop = brown + yellow
    
    k = math.floor(gop/3)
    for i in range(3, k+1):
        x = i
        y = hap - x
        
        if (y>=3 and x*y == gop):
            if (x>=y):
                answer.append(x)
                answer.append(y)
            else:
                answer.append(y)
                answer.append(x)
            break

    return answer
