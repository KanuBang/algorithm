# 해시 테이블 - 딕셔너리
dict = {}

# 해시 테이블 - 숫자 배열일 경우
arr = [1,2,3,4,5,6] # arr의 각 원소를 hash_table의 키 값으로 활용
hash_table = [0] * (len(arr)+1)

# arr의 원소가 hash_table의 key 값이라면 value를 1로 update
for i in arr:
    print(i)
    hash_table[i] = 1

print(hash_table)