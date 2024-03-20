'''
#1. 키워드: 행렬
#2. 제약조건: 행렬 열의 길이는 100이하, 곱할 수 있는 배열만 주어진다.
#3. 의사코드:

    arr1의 행의 개수 3, arr2의 열의 개수 2
    기본로직
    1. arr1에서 1번째 행을 뽑는다.
    2. arr2의 1번째, 열을 뽑는다.
    3. arr1과 각 자리를 곱한다.
    4. arr2의 2번째 열을 뽑는다.
    5. arr1과 각 자리를 곱한다.
    6. 1차원 배열에 값을 넣어 answer에 추가한다.
'''

def solution(arr1, arr2):
    
    # 행렬 arr1과 arr2의 행과 열의 수
    r1, c1 = len(arr1), len(arr1[0]) # 3 / 2
    r2, c2 = len(arr2), len(arr2[0]) # 2 / 2
    
    # 3 * 2 행렬과 2 * 2 행렬의 곱셈의 크기는 3(r1) * 2(c2)
    # 결과를 저장할 2차원 리스트 초기화
    ret = [[0] * c2 for _ in range(r1)]
    
    # arr1의 각 행과 arr2의 각 열에 대해
    for i in range(r1):
        for j in range(c2):
            # 두 행렬의 데이터를 곱해 결과 리스트에 더함
            for k in range(c1):
                ret[i][j] += arr1[i][k] * arr2[k][j]
    
    return ret