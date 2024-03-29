def solution(want,number,discount):
    # want 리스트를 딕셔너리로 변환
    want_dict = {}
    for i in range(len(want)):
        want_dict[want[i]] = number[i]

    answer = 0

    for i in range(len(discount) - 9):
        discount_10d = {}


        for j in range(i, i+10):
            if discount[j] in want_dict:
                discount_10d[discount[j]] = discount_10d.get(discount[j],0) + 1

        if discount_10d == want_dict:
            answer += 1

    return answer

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
print(solution(want,number,discount))

dic = {1:2, 3:4}
print(dic.get(4))
print(dic.get(3))
print(dic.get(4), 0)


