# 초보자 프로그래머 홍길동은 사용자가 입력한 양의정수(범위는 int)
# 각 자리수를 더해 출력하는 프로그램을 만들고 싶어한다. 
# ex) 5923의 결과는 5+9+2+3인 19이다 ex) 200의 결과는 2+0+0인 2이다 
# ex) 6719283의 결과는 6+7+1+9+2+8+3인 36이다.

# for문
def number(x):
    y = 0
    for i in str(x):
        y += int(i)
    print(y)



# eval 함수
def number2(x):
    print(eval("+".join(str(x))))