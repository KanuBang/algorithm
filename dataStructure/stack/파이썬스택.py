'''
파이썬의 리스트 특징과 스택의 연관성
1. 파이썬는 리스트 크기를 동적으로 관리하므로 isFull, isEmpty를 구현할 필요 없음.
2. push는 append, pop은 pop을 호출하는 게 전부임.
따라서, 파이썬의 리스트는 다음과 같이 구현된다.
'''

stack = []

# 데이터 추가
stack.append(1)
stack.append(2)
stack.append(3)

# 스택에서 데이터 꺼냄
stack.pop()
stack.pop()

# 스택의 크기를 구함
len(stack)
