stack = [] # 스택 리스트 초기화
max_size = 10 # 스택의 최대 크기

def isFull(stack):
    #스택이 가득 찼는 지 확인하는 함수
    return len(stack) == max_size

def isEmpty(stack):
    #스택이 비었는 지 확인하는 함수
    return len(stack) == 0

#스택에 데이터 추가
def push(stack, item):
    if isFull(stack):
        print("스택이 가득 찼습니다.")

    else:
        stack.append(item)
        print("데이터가 추가 되었습니다")


# 스택에서 데이터 꺼내기
def pop(stack, item):
    if isEmpty(stack):
        print("스택이 비었습니다.")
        return None
    else:
        return stack.pop()


