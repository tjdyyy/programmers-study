### 풀이
citations 배열을 정렬한 후, `h`를 0부터 하나씩 올려 왼쪽부터 h가 되는지를 검사한다.

예를 들어 citations가 `[3, 0, 6, 1, 5]`일 때, 정렬을 하면 `[0, 1, 3, 5, 6]`이 되고, 왼쪽에서부터 h보다 배열 각각의 값이 큰지를 검사해 어느 지점에서 h보다 큰 값들을 가지는 지를 센다.

#### h가 3일 때

|h보다 큰지|0|1|3|5|6|
|-|-|-|-|-|-|
|X|X|O|O|O|


이렇게 되면 `3`번 이상 인용된 논문의 개수인 `count`가 3이기 때문에 `3`편 이상이다.
이 때 나머지 논문이 h번 이하 이용되어야 하기 때문에, `citations.length - count >= h`를 통해 확인할 수 있다.

이런 식으로 h가 되는지를 확인하고 그 중 최댓값을 리턴하면 된다.

#### 시간 복잡도
for문을 두 번이나 사용했기 때문에 O(n^2)인데, 논문의 수와 인용 횟수가 적기 때문에 무리없이 통과할 수 있었다.

### 소스 코드

```java
import java.util.*;
class Solution {
    public int solution(int[] citations) {
        int max = 0;
        Arrays.sort(citations);
        for (int h=0; h<=citations[citations.length - 1]; h++) {
            int count = 0;
            for (int i=0; i<=citations.length - 1; i++) {
                if (h <= citations[i]) {
                    if (citations.length - count >= h) {
                        max = Math.max(max, h);
                    }
                    break;
                }
                count++;
            }
        }
        return max;
    }
}
```