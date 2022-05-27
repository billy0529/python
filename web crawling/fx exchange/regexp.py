import re

s = "hi!!!!!"
print(re.match(r"hi!+",s))

s1 = "lovelovelove"
print(re.match(r"ovel",s1)) # unmatch
print(re.match(r"love",s1)) # love match
print(re.search(r"ovel",s1)) # ovel match
print(re.findall(r"ovel",s1)) # ovel, ovel 2개 반환