'''
1. 전화번호 길이 목록을 구한다.
'''
def solution(phone_book):
    
    # 1. 전화번호 길이 목록을 구한다. 같은 길이는 중복 제거
    length = list(set([len(number) for number in phone_book]))
    dic = {}
    
    # 2. key:전화번호, value: 해당 key를 접두사로 하는 경우 count
    for prefix in phone_book:
        dic[prefix] = 0
    
    for size in length:
        for number in phone_book:
            
            if size <= len(number):
                
                key = number[0:size]
                
                if key in dic:
                    dic[key] += 1
                    
                    if dic[key] == 2:
                            return False
                
    
    return True

'''
['22224', '22225', '2222']
'''