### 풀이

리스트의 원소의 value가 N이면 안입거나, 1개 입거나, 2개 입거나, ..., N개 입거나를 선택하는 것이기 때문에 그 경우의 수는 N + 1이고, 리스트 원소 각각을 이런 식으로 경우의 수를 구해 모두를 곱해주면 된다.

#### 시간 복잡도
for문을 1번, clothes의 길이만큼 사용하므로 시간 복잡도는 O(N)이다.

### 소스 코드

```java
import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        Map<String, Integer> map = new HashMap<>();
        for (int i=0; i<clothes.length; i++) {
            if (map.containsKey(clothes[i][1])) {
                map.replace(clothes[i][1],map.get(clothes[i][1]) + 1);
            } else {
                map.put(clothes[i][1], 1);
            }
        }
        for (String k : map.keySet()) {
            answer *= map.get(k) + 1;
        }
        return answer - 1;
    }
}
```