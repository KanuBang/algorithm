'''
키워드: 문자열, 올바른 괄호 문자열, 왼쪽으로 회전, 올바른 괄호 문자열이 되게 하는 x의 개수
제약조건: 1 이상 1000 이하
테스트케이스:
[](){}
문자가 6개 -> 5번 왼쪽 회전

의사코드:
1. 왼쪽으로 회전시킨다.
1-1 새로운 문자열 객체를 생성한다.
1-2 1부터 끝까지를 슬라이싱하여 새로운 문자열에 붙인다.
1-3 0번째를 인덱싱하여 새로운 문자열 끝에 붙인다.

2. 올바른 괄호 문자열인지 확인한다.
2-1 [, (, { 은 스택에 push
2-2 ], ), } 가 나오면 스택 pop
2-3 짝이 맞다면 pass, 안 맞다면 break

3. 2의 과정에서 짝이 모두 맞았다면, answer를 1증가시킨다.
'''
def solution(s):
    answer = 0
    stack = []
    if len(s) == 1:
        return answer
    
    for i in range(0, len(s)):
        
        result = True
        
        if i > 0:
            tmp = s
            s = tmp[1:] + tmp[0]
        
        for j in s:
            
            if j == '[' or j == '(' or j == '{':
                stack.append(j)
            
            elif len(stack) == 0 and j in [']', '}', ')']:
                    result = False
                    break

            else:
                top = stack[-1]
                if top == '[' and j ==']':
                    stack.pop()    
                elif top == '{' and j =='}':
                    stack.pop()
                elif top == '(' and j ==')':
                    stack.pop()
                else:
                    result = False
                    break
        
        if result == True:
            answer += 1
                    
    return answer