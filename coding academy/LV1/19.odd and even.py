# 홀수와 짝수의 개수를 구하는 프로그램을 만들어라.# 
# [3, 4, 5, 6, 7]
# = 홀수 3개, 짝수 2개
# [12, 16, 22, 24, 29]
# = 홀수 1개, 짝수 4개 
# [41, 43, 45, 47, 49]
# = 홀수 5개, 짝수 0개# 
# 홀수 : 2로 나누어 떨어지지 않는 정수
# 짝수 : 2로 나누어 떨어지는 정수

def numbers(x):
    odd, even = 0, 0
    for i in x:
        if i & 1 == 0:
            even += 1
        else:
            odd += 1
    print("Even numbers are {}, Odd numbers are {}".format(even,odd))