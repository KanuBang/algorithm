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
