## 위장 | python | tjdyyy | 21.07.26

### 코드 설명

java 풀이> https://blog.naver.com/tjdyyy/222376249384

카펫의 가로를 x, 세로를 y라고 하자. 갈색 영역은 2*x +2*(y-2)이고, 노란색 영역은 x*y에서 갈색 영역을 뺀 것이다. 
x, y에 대해 정리하면 x+y = (brown + 4) / 2이고 x*y = brown + yellow이다.

노란색 영역이 1이상이므로 가로와 세로는 3이상이다. x의 역할을 하는 for문의 반복 변수 i의 범위를 3부터 x*y/3이하로 지정한다. 
이때 y도 3이상이고, x*y 가 brown+yellow와 같으면 answer에 x, y를 저장하고 for문을 break을 통해 종료한다.

### 시간 복잡도

for문이 한 번 사용되므로 시간 복잡도는 O(n)이다.

```{.python}
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
```
