# 배열 [1,2,3,4]에서 자기 자신과의 연산을 피하는 방법
# 각 요소에서 자신보다 뒤에 있는 요소를 선택하면 된다.

a = [1,2,3,4]
arr = []
for i in range(len(a)):
    for j in range(i+1, len(a)):
        print(f"i: {i}, j: {j}")