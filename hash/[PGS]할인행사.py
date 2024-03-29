'''
#키워드: 
1. 정현이는 자신이 원하는 제품과 수량이 할인하는 날짜와 
10일 연속으로 일치할 경우에 맞춰서 회원가입을 하려 합니다.

정현이가 원하는 제품이 바나나 3개, 사과 2개, 쌀 2개, 돼지고기 2개, 냄비 1개이며, 
XYZ 마트에서 14일간 회원을 대상으로 할인하는 제품이 날짜 순서대로 

1    2      3   4    5  6     7
치킨, 사과, 사과, 바나나, 쌀, 사과, 돼지고기, 
바나나, 돼지고기, 쌀, 냄비, 바나나, 사과, 바나나


3 사과, 바나나, 쌀, 사과, 돼지고기, 바나나, 돼지고기, 쌀, 냄비, 바나나
4 바나나, 쌀, 사과, 돼지고기, 바나나, 돼지고기, 쌀, 냄비, 바나나, 사과
모두 할인 받을 수 있는 회원등록 날짜의 총 일수를 return

# 제한조건과 TC
생각보다 discount 길이가 큼 -> N^2은 불가해보임

# 테케 분석
-단순하게 생각하면 이중 for문인데 이러면 시간복잡도가 터질 거 간다.
-해시 사용 -> key 과일 value 필요한 개수

# 히든테케
- want의 길이가 1
- discount하는 항목이 다 똑같음

# 의사 코드
1. 해쉬 테이블 만들기: key 과일 value 필요한 개수

banana:3, apple:2, rice:2, pork:2, pot:1
"apple", "banana", "rice", "apple", "pork", 
"banana", "pork", "rice", "pot", "banana",

2. discount를 10일 단위로 끊어서 배열을 만든다.
3. 만든 배열로 순회한다.
3-1 같은게 있다면 -> 모든 해시의 value가 0이 되면 result += 1
3-2 같은게 없다면 
'''
def solution(want, number, discount):
    answer = 0
    n = len(want)
    dic = {}
    
    # 1. 해쉬 테이블 만들기: key 과일 value 필요한 개수
    for i in range(n):
        dic[want[i]] = number[i]
    
    # 2. discount를 10일 단위로 끊어서 배열을 만든다.
    start = 0
    end = 10
    
    while end <= len(discount):
        result = True
        # 원본 해시가 보존을 위헤 연산은 독립적으로 복사된 해시를 이용
        copy_dic = dict(dic)
        
        # 할인 행사에 맞는 물품이 있다면 number -1
        for key in discount[start:end]:
            if key in copy_dic:
                copy_dic[key] -= 1
        
        # 할인 행사에서 원하는 물품을 다 구할 수 있는지 체크한다.
        for key in want:
            if copy_dic[key] != 0:
                result = False
                break
        
        # 할인 행사에서 원하는 물픔을 다 구할 수 있다면 answer += 1
        if result == True:
            answer += 1
            
        start += 1
        end += 1
        
    return answer