'''
#키워드:  쌍의 개수를 출력한다.
#제한조건: 입력의 크기가 유난히 크다.
#시간복잡도: O(N^2)은 절대 불가능이다.
#테스케이스:
-입력:                  -출력:
9                       3
5 12 7 10 9 1 2 3 11    
13

키 값
1  1
2  1
3  1
4
5  1
6
7  1
8  
9  1
10 1
11 1
12 1
13


12,1 / 10,3 / 11,1 -> 3개
#
# 의사코드
1. 정보를 입력받는다.
2. 숫자의 유무를 나타내는 해쉬테이블을 만든다.
3. 각 숫자가 필요한 target을 만들기 위한 필요한 숫자가 있는 지 해쉬 테이블일 이용해 확인한다.
'''

# 1. 정보를 입력받는다.
n = int(input())
arr = input()
nums = list(map(int, arr.split()))
target = int(input())
hash_table = [0] * (2000000)
cnt = 0

# 2. 숫자의 유무를 나타내는 해쉬테이블을 만든다.
for num in nums:
    hash_table[num] = 1

for num in nums:

    if hash_table[target-num] == 1:
        cnt += 1

print(cnt // 2)



