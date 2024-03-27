'''
#키워드: 딱히...
#제약조건: 배열도 짧고, 문자열도 짧고 딱히...
#시간복잡도: n^2도 가능해 보임.
#테스트케이스 분석:
cards1: [i, drink, water] 
cards2: [want, to] 
goal: [i, want, to, drink, water]

1. goal에서 deque를 하면 i가 나온다.
2. cards1[0] 와 cards2[0] 중 하나가 i이면 OK -> 그리고 deque
NOT OKAY 이면 NO & break
3. 12를 반복

# 특수케이스
1. cards를 다 써버린 경우는 front를 확인할 수 없다.
2. goal에서 뺀 단어가 cards1, cards2 둘에 있는 경우

# 의사코드
0. cards1과 cards2의 가짜 front 변수를 각각 선언한다.
1. goal에서 deque
2. cards1 과 card2에 뽑힌 단어가
2-1 둘 중 하나라도 있다면 -> front 변수 + 1
2-2 아무도 없다면 -> NO 리턴후 종료 
'''
from collections import deque
def solution(cards1, cards2, goal):
    answer = "Yes"
    # 0. cards1과 cards2의 가짜 front 변수를 각각 선언한다.
    front_1, front_2 = (0,0)
    goal = deque(goal)
    
    while goal:
        # goal에서 deque
        word = goal.popleft()
        
        # cards1 과 card2에 뽑힌 단어가 둘 중 하나라도 있다면 -> front 변수 + 1
        if front_1 != len(cards1) and cards1[front_1] == word:
            front_1 += 1
         
        elif front_2 != len(cards2) and cards2[front_2] == word:
            front_2 += 1
        
        # 아무도 없다면 -> answer = "No"
        else:
            answer = "No"
            break
    
    return answer