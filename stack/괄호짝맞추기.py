'''
1. clue: 닫힌 괄호는 직전의 가장 가깝게 열린 괄호와 상쇄된다.
2. 제약조건: 딱히 없는 문제
3. 테케분석:
(())() -> true
4. 의사코드
#1. 열린 괄호를 stack에 넣는다
#2. 닫힌 괄호가 나오는 순간 pop
#3. 1~2 과정을 반복해서 stack이 비어있다면 짝이 맞는 거고 아니면 짝이 안 맞음
'''

def solution(s):
    stack = []
    
    for c in s:

        if c == "(":
            stack.append(c)

        elif c == ")":
            if not stack:
                return False
            else:
                stack.pop()

    #스택이 비었으면
    if not stack:
        return True
    
    else:
        return False
    


s = "(())("
print(solution(s))