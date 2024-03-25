'''
1. 키워드: 10진수를 2진수로 변환
2. 제약조건: 없음
3. 테스트케이스:
4. 의사코드
#1 2로 나눈다.
#2 나머지를 스택에 push, 숫자는 몫으로 수정한다.
#3 몫이 0이 되면 종료한다.
#4 스택 탑을 pop해서 문자열에 붙인다.
#5 정답을 출려한다.
5. 특수 케이스

1 -> 0
'''


def solution(decimal):
    stack  = []
    ans = ""
    while decimal != 0:
        stack.append(str(decimal % 2))
        decimal //= 2

        if decimal == 0:
            break
    '''
    while stack:
        ans += str(stack.pop())
    '''

    ans = ''.join(stack)
    return ans

decimal = 12345
print(solution(decimal))
