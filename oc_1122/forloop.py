a = {"김도한" : "010-7178-9999", "신봉건" : "010-9798-8888"}

for name in a :
    print(name)

for key in a.keys():
    print(key)
for item in a.items():
    print(item)

# range 함수를 이용하여 List 생성
a = range(10)
print(type(a))

for i in a:
    print(i)