# 기본 정렬
my_list = [3,4,2,1]
sorted_list1 = sorted(my_list)
print(sorted_list1)

# reverse = True -> 내림차순 정렬
sorted_list2 = sorted(my_list, reverse=True)
print(sorted_list2)

# key로 정렬 기준 정하기
rates = [['wirtz', 8.8], ['grimaldo', 9], ['xhaka', 7.3], ['hincapie',8]]
sorted_list3 = sorted(rates, key=lambda x: x[1], reverse=True) 
print(sorted_list3)


# dict 정렬하기
dict = {'wirtz': 8.8, 'grimaldo': 9, 'xhaka': 7.3, 'hincapie':8}
result = sorted(dict, key = lambda x : dict[x], reverse=True)
print(result)


dict = {
    	2: 3,
    	1: 3,
    	3: 5,
    	6: 3,
    	5: 2
}




my_dict = {'apple': 3, 'banana': 1, 'cherry': 2}

# 딕셔너리의 값을 기준으로 정렬하여 (key, value) 튜플의 리스트를 생성합니다.
sorted_items = sorted(my_dict.items(), key=lambda x: x[1])

# 정렬된 (key, value) 튜플 리스트에서 키만 추출하여 리스트로 만듭니다.
sorted_keys = [item[0] for item in sorted_items]

print(sorted_keys)