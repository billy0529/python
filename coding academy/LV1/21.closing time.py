# 현우는 성인이되어 회사에입사했다.
# 하지만 들어간기업이 하필 할일없는 중소기업이라
# 퇴근시간까지 놀다가 퇴근시간에 퇴근하는것이 일상화가되어버렸다..
# 현우는 심심한지라 좀더효율적으로놀기위해
# 현재부터 퇴근시간까지 남은시간을 알려주는 계산기를 만들어
# 계산적으로놀고싶었다 우리가현우를 도와주자!!
# (참고로 현우의퇴근시간은 17시30분이다)
# input: 현재시간
# output: 남은시간 : hh:mm:ss
# or
# 남은시간 : s
# 심화버젼 : 이쁘게꾸며보자


def current_time(time):
    time = time.split(":")
    time[0] = str(17 - int(time[0]))
    if int(time[1]) >= 31:
        time[1] = str(60 - int(time[1]))
        time[0] = str(int(time[0]) - 1)
    else: 
        time[1] = str(int(30 - int(time[1])))
    if int(time[2]) > 0:
        time[2] = str(60 - int(time[2]))
        time[1] = str(int(time[1]) - 1)
    if int(time[0]) <= 9:
        time[0] = "0" + time[0]
    if int(time[1]) <= 9:
        time[1] = "0" + time[1]
    print("남은시간>>> {}:{}:{}".format(time[0],time[1],time[2]))

current_time("16:00:00")


# datetime module
import datetime as dt   # dt 로 alias

cur_time = dt.datetime.today()  # 현재시간
leave_time = cur_time.replace(hour=17, minute=30, second=0)  # 퇴근시간
# 남은 시간 계산 (퇴근 시간이 지난 경우 익일 퇴근까지의 시간)
diffsec = (leave_time - cur_time).total_seconds()
diffsec = diffsec + 60 * 60 * 24 if diffsec < 0 else diffsec

print(f"다음 퇴근시간까지는 {dt.timedelta(seconds=diffsec)}({diffsec:,.0f}초) 남았습니다.")
