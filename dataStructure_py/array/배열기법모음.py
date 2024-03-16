# 리스트 컴프리헨션으로 특정 연산 적용하여 배열 생성
numbers = [1,2,3]
squares = [i ** 2 for i in numbers]

# 배열의 길이를 반환 -> len(list)
len(numbers) # 3

# 배열이 등장하는 첫 번째 인덱스를 반환 -> index(data)
numbers.index(3)

# 데이터 개수 카운트 -> count(data)
numbers.count(2)

# 정렬하기 -> sort()
# default 값은 오름차순 정렬이다. (reverse=False)
# 내림차순 정렬은 reverse=True
numbers.sort(reverse=True) # [3,2,1]