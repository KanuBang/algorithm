'''
16분 + 20 = 36분 컷!

키워드: 동적?, 실패율을 구해라
제약조건:
1. 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어 수 / 스테이지에 도달한 플레이어 수
2. N = 스테이지의 개수 (500이하 자연수)
3. stages 배열 -> 시용자가 현재 멈춰있는 스테이지의 번호 (200000이하 자연수)
3. 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return

크기를 보면 N, len(stages)로 O(n^2) 나오면 시간 초과일 듯
O(n)으로 짜자.

의사코드:
1. 사용자 수를 구한다.
2. 몇 명이 i번째(1~N) 스테이지에 실패했는 지 확인한다.
3. 실패율을 구한다.
4. i를 key로 실패율을 value로 하는 dict을 만든다.
5. 1~4를 마친 후 내림차순 정렬 후 리턴
'''

'''
테스케이스: 특수한 상황을 검증해보자.
N = 4 stages = [5,5,5,5,5]

실패율 1: 0 / 5
실패율 2: 0 / 5
실패율 3: 0 / 5
실패율 4: 0 / 5


N = 4 stages = [1,1,1,1,1]
실패율 1: 5 / 5
실패율 2: 0 / 0 (devision by zero 런타임 에러 발생)
실패율 3: 0 / 0
실패율 4: 0 / 0
'''
def solution(N, stages):
    answer = []
    user = len(stages)
    score = []
    for i in range(1, N+1):
        unclear = stages.count(i)
        #예외 처리
        if user == 0:
            fail = 0
        else:
            fail = unclear / user
        score.append(fail)
        user -= unclear
    
    size = len(score)
    # [0 0 0 0]
    
    for j in range(size):
        max_v = max(score)
        tmp_idx = score.index(max_v)
        answer.append(tmp_idx+1)
        score[tmp_idx] = -1
        
    
    return answer