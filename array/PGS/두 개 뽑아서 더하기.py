'''

복잡도: 길이가 100개이다. O(n^2)이여도 최대 연산 횟수가 10000니까 n^2도 괜찮아 보인다.
케이스: [1,1,1,1] -> [2]
키워드: 배열, 오름차순

1. 배열의 요소를 순차적으로 하나 고정한다.

2. 1번에 고정한 요소에 다른 배열 요소를 순차적으로 더한다.
2-1 자기 자신 과는 덧셈 하지 않는다.

3. 2번에서 나온 값이 answer에 추가한다.
3-1 이미 존재한다면, 추가하지 않는다.
3-2 존재하지 않으면, 추가한다.

4. 오름차순 정렬한다.
'''

def solution(numbers):
    answer = []
    length = len(numbers)
    
    for i in range(length):
        fix = numbers[i]
        
        for j in range(length):
            
            if i == j:
                continue
            
            data = fix + numbers[j]
        
            if data not in answer:
                answer.append(data)
                
    answer.sort()
    return answer