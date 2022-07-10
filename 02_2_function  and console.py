# 수학의 함수랑 거의 유사 하다
def f_x(x):
    return 2*x + 7

def g_x(x):
    return x**2

print(f_x(2)) # argument가 2임. f_x의 parameter는 2임
print(g_x(2))
print(f_x(g_x(2)))
print(g_x(f_x(2)))

# 리턴값이 있는것과 없는것
def f_test(x):
    print("x")

test01 = f_test(1)
print(test01) # None 아무것도 없다


'''
%-format, str.format, f-string
f-string 많이 쓴다. PEP498에 근거한 formatting기법이다.

#%-format
print('%s %s ' % ('one','two')) # old 한 방식
print('%d %d ' % (1, 2)) # old 한 방식

#str.format
print('{} {}}'.format('one','two)) # old 한 방식

#f-string
name= "Sungchul"
age = 39
print(f'Hello, {name}. you are {age}.')
print()
print(f'{name:20}') # 20칸. 왼쪽정렬이 기본
print(f'{name:>20}') # 20칸. 오른쪽정렬
print(f'{name:*>20}') # 20칸. 오른쪽정렬 남은칸은*로 채움
print(f'{name:^20}') # 20칸. 가운데 정렬
number=3.1415926535
print(f'{number:.2f}') # 소수점2번쨰자리까지출력
'''

'''
lab: 화씨변환기 python fahrenheit.py
섭씨 변환공식은 ((9/5) * 섭씨온도) + 32 
'''
 