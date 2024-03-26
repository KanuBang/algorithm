# 32분 걸림
# 20분만 곹부 더하자
'''
1. 키워드: 같은 알파벳이 2개 붙어 있는 짝 -> 제거 -> 남은 거 연결 : 이렇게 해서 모두 제거되면 1 반환, 안되면 0 반환
2. 제약조건: 1000000 이하의 자연수
3. 시간복잡도: n으로 짜야함.
4. 테스크케이스:
특수: 길이가 1인 경우

b -> ba -> baa -> b -> bb -> "" -> a -> aa -> ""
5. 의사코드

#1. 길이를 체크한다. 
1-1. 1이면 바로 0 반환
1-2. 1이 아니면 첫 번째 문자를 stack에 push

#2. stack의 top과 현재 문자를 비교한다.
#2-1 스택이 비어있지 않다.
    #2-1-1. 같다 -> top을 pop 한다.
    #2-1-2. 다르다 -> 현재 문자를 push 한다.
#2-2 스택이 비어있다.
    #2-2-1. 현재 문자를 push 한다.
    
#3. stack의 크기를 비교한다.
3-1 길이가 0이다. -> 1 반환
3-2 길이가 1이다. -> 0 반환
'''

def solution(s):
    answer = -1
    n = len(s)
    stack = []

    if n == 1:
        return 0
    
    stack.append(s[0])
    
    
    for i in range(1,n):
        char = s[i]
        
        if stack:
            top = stack[-1]
            if top == char:
                stack.pop()
            else:
                stack.append(char)
        
        else:
            stack.append(char)
    
    if not stack:
        answer = 1
    else:
        answer = 0
    
    return answer