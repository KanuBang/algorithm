'''
키워드: 찍는 방식의 규칙성
제약조건: 10000문제, 정답은 1~5중 하나, 가장 높은 점수를 받은 사람이 여럿일 경우 오름차순 정렬
시간복잡도: O(n^2)은 1억번 연산하므로 O(n) 권장

의사코드(기능 중심)
1. 수포자들이 찍는 방식을 저장한다.
2. 답과 비교한다.
3. 수포자들이 맞춘 문제의 개수를 저장한다.
4. 가장 높은 점수를 받은 사람을 찾는다. (동점일 경우 오름차순 정렬한다.)
'''

def solution(answers):
    answer = []
    
    a = [1,2,3,4,5] * 2000
    b = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    score = [0,0,0]
    
    for i, value in enumerate(answers):
        if a[i] == value:
            score[0] += 1
        if b[i] == value:
            score[1] += 1
        if c[i] == value:
            score[2] += 1
            
    high_score = max(score)
    
    for j in range(len(score)):
        if score[j] == high_score:
            answer.append(j+1)
    
    return answer