## H-index | python | tjdyyy | 21.07.04

### 코드 설명

java 풀이 > https://github.com/tjdyyy/Programmers/blob/master/java/sort/(level2)%20H-index

스터디 공통 문제로 선정되어 파이썬으로 풀어보았다. 


citations 배열을 순서대로 정렬하면, n 번 이상 인용된 논문의 개수를 따로 셀 필요가 없다. 

for문 > citations의 원소를 h로 저장하고, 반복 시 length 값을 1씩 줄여 h번 이상 인용된 논문을 나타냈다.

if문 > h가 length보다 크거나 같으면 h번 이상 인용된 논문이 length개인 것이다. 이것은 length번 이상 인용된 논문이 length개 인 것으로 볼 수 있다. 따라서 H-index값은 length이므로 length 값을 return한다.

만약 조건에 맞는 H-index값이 없으면 0을 return한다. 


### 시간 복잡도

파이썬 리스트 sort는 O(n log(n))의 시간 복잡도를 가진다고 한다. 

for문은 n번 반복하기 때문에 O(n)의 시간 복잡도를 가진다.

n < n log(n) 이므로 이 코드는 O(n log(n))의 시간 복잡도를 가진다. 
