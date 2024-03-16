'''

파이썬의 enumerate() 함수는 반복 가능한(iterable) 객체(예: 리스트, 튜플, 문자열 등)를 
입력으로 받아 각 항목의 인덱스와 값을 포함하는 enumerate 객체를 반환합니다. 
이 객체는 이후 반복문에서 사용할 수 있습니다.

'''

my_list = ['apple', 'banana', 'orange']

for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")

'''

여기서 enumerate() 함수는 각 요소와 해당 요소의 인덱스를 튜플 형태로 반환합니다. 
이를 for 루프에서 index, value와 같이 두 변수에 대입하여 받아들이고, 각각을 출력하는 예시입니다.
'''