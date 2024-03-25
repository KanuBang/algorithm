'''
1. 키워드: 초 단위로 기록된 주식 가격, 가격이 떨어지지 않은 기간
2. 제약조건: 2이상 100000 이하 길이 
3. 시간복잡도: n이 합당
4. 테스테케이스:
#특수한 상황
[4,3,2,1], [1,1,1,1]

5. 의사코드

들어가기 앞서...
이중 for문으로 바깥에서 잡고, 안쪽에서 순차대로 비교해도 되긴 하는데 이러면... 효율이 시간복잡도가 n^2이 됨.
stack으로 pop하면서 하면... 배열 길이가 줄어드는 것을 노리는 거 같기도 하다.

# 1. 스택을 만든다.
# 2. top과 stack 숫자를 비교한다.
    # 2-1. 요소가 top보다 작다. -> break
    # 2-2. 요소가 top보다 크거나 같다. -> 1증가
# 3. answer에 push
'''
def solution(prices):
    answer = []
    stack = list(reversed(prices))
    
    while stack:
        top = stack.pop()
        cnt = 0
        
        for i in range(len(stack)-1,-1,-1):
            if stack[i] < top:
                cnt += 1
                break
            else:
                cnt += 1      
        answer.append(cnt)
    
    
    return answer


'''
최악의 경우
1. [1, ... 9999,10000] 길이는 100,000
2.  (99999 + 1) / 2
n-1 * n
'''