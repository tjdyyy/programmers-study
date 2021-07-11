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