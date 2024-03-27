'''
1. 키워드: 앞에 있는 모든 기능이 완성되지 않으면 배포가 불가능하다.
2. 제약조건: 두 배열 모든 100이하의 크기
3. 시간복잡도: 널널한 듯
4. 테스트케이스:
특수: 동시에 모두 다 끝나는 상황?
5. 의사코드
93 30 55
94 60 60
95 90 65
96 100 70
97 100 75
98 100 80
99 100 85
100 100 85 -> if front is 1000 -> popleft -> 2
85 -> 90 -> 95 -> 100
#1 progresses의 각 요소에 speeds 각 요소를 더한다.
#2 만약 어떤 프로그레스가 100이 넘는다면 100으로 고정한다.
#3 매턴 마다 front가 100인지 확인한다
#3-1 100이면 popleft, 다음것도 100이면 popleft
#3-2 그 개수를 answer에 append
'''
from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque(progresses)
    speed_q = deque(speeds)
    
    # 모든 작업이 완료될 때가지 반복한다.ㄴ
    while queue:
        cnt = 0
        n = len(queue)
        
        # 하루 기준으로 진행 프로그레스 업ㅔ이트
        for i in range(n):
            queue[i] += speed_q[i]
            if queue[i] >= 100:
                queue[i] = 100
        
        # 큐의 프론트, 즉, 가장 앞의 작업이 완수 되었다면 프로세스에서 빠져나간다
        # 반복해서 뒤의 작업도 완료 되었는지 확인한다.
        # cnt로 완료된 작업 수를 카운트한다.
        while queue[0] == 100 and queue:
            queue.popleft()
            speed_q.popleft()
            cnt += 1
        
        # 완료된 작업 수를 answer에 넣는다.
        if cnt != 0:
            answer.append(cnt)
        
    return answer

print(solution([93, 30, 55], [1, 30, 5]))