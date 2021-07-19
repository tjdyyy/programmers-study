def solution(clothes):
    answer = 1
    
    dic = {} # 딕셔너리 사용
    
    for list in clothes:
        if list[1] in dic: # 딕셔너리에 옷 종류가 있으면
            dic[list[1]] += 1 # 값 증가
        else: # 없으면
            dic[list[1]] = 1 # 딕셔너리 생성
        
    for i in dic.values():
        answer *= (i+1) # 종류 별 개수 + 1씩 곱함
        
    return answer-1 # 아무것도 안 입는 경우 -1을 뺌
