a = 3
b = 2
print(a**b)
print(a%b)

a = 11.5
print(a)

a = 'madchick'
print(a)

a = True
print(a)

a = (3==2)
print(a)

a = '2'
b = str(2)
print(a+b)
print(len(a+b))



text = 'abcdefghijk'
result = text[:3]
print(result)
result = text[3:]
print(result)
result = text[3:8]
print(result)
result = text[:] # 전체
print(result)

myemail = 'madchick@gmail.com'
result = myemail.split('@')[1].split('.')[0]
print(result)



a_list = [2, '배', True, ['사과','감']]
print(a_list[3][1])
a_list.append(99)
print(a_list[:3])
print(a_list[3:])
print(a_list[-1]) # 맨 마지막

a_list = [1,5,6,2,3]
a_list.sort(reverse=True)
print(a_list)
print(99 in a_list)



# 딕셔너리
a_dict = {'name':'bob', 'age':27, 'friend':['영희','철수']}
print(a_dict['friend'][1])

print('height' in a_dict)
a_dict['height'] = 188
print(a_dict)



people = [
    {'name': 'bob', 'age': 20, 'score':{'math':90,'science':70}},
    {'name': 'carry', 'age': 38, 'score':{'math':40,'science':72}},
    {'name': 'smith', 'age': 28, 'score':{'math':80,'science':90}},
    {'name': 'john', 'age': 34, 'score':{'math':75,'science':100}}
]
print(people[1]['age'])
print(people[2]['score']['science'])



money = 2000
if money > 3800:
    print('택시를 타자')
elif money > 1200:
    print('버스를 타자')
else:
    print('택시를 못타')
print('그럼 뭘 타지?')



fruits = ['사과', '배', '감', '수박', '딸기']
for fruit in fruits:
    print(fruit)

people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

for person in people:
    name = person['name']
    age = person['age']
    if age > 20:
        print(name, age)

for i, person in enumerate(people):
    name = person['name']
    age = person['age']
    print(i, name, age)
    if i > 3:
        break



num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]

for num in num_list:
    if num % 2 ==0:
        print(num)

count = 0
for num in num_list:
    if num % 2 ==0:
        count += 1
print(count)

sum = 0
for num in num_list:
    sum += num
print(sum)

max = 0
for num in num_list:
    if max < num:
        max = num
print(max)



def sum(a,b):
    print('\n더하기를 하셨네요.')
    return a + b

result = sum(1,2)
print(result)

def check_gender(pin):
    num = pin.split('-')[1][:1]
    if int(num) % 2 == 0:
        print('여성')
    else:
        print('남성')

check_gender('123456-1023123')
check_gender('123456-2023123')
check_gender('123456-3023123')
check_gender('123456-4023123')



a = ('사과','감','배') # 리스트와 동일, 튜플은 불변형
print(a[1])

people = [('bob',27),('john',30)]
print(people)

a = [1,2,3,1,2,3,1,2,3]
a_set = set(a) # set은 중복을 제거
print(a_set)

a = ['사과','감','수박','참외','딸기']
b = ['사과','멜론','청포도','토마토','참외']
a_set = set(a)
b_set = set(b)
print(a_set & b_set)  # 교집합
print(a_set | b_set)  # 합집합

student_a = ['물리2','국어','수학1','음악','화학1','화학2','체육']
student_b = ['물리1','수학1','미술','화학2','체육']
a_set = set(student_a)
b_set = set(student_b)
print(a_set - b_set) # 차집합



scores = [
    {'name':'영수','score':70},
    {'name':'영희','score':65},
    {'name':'기찬','score':75},
    {'name':'희수','score':23},
    {'name':'서경','score':99},
    {'name':'미주','score':100},
    {'name':'병태','score':32}    
]

# f-string
for s in scores:
    name = s['name']
    score = s['score']
    print(name + '의 점수는 ' + str(score) + '점 입니다.')
    print(f'{name}의 점수는 {score}점 입니다.')



people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby'},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

for person in people:
    try:
        if person['age'] > 20:
            print (person['name'])
    except:
        name = person['name']
        print(f'{name} - 에러입니다')



# 다른 파일에서 함수 불러오기
# from 파일명 import * (또는 함수명)



num = 3
result = "짝수" if num%2 == 0 else "홀수"
print(f"{num}은 {result}입니다.")

a_list  = [1, 3, 2, 5, 1, 2]
b_list = [a*2 for a in a_list]
print(b_list)



people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

def check_adult(person):
    return '성인' if person['age'] > 20 else '청소년'

result = map(check_adult, people)
print(result)
print(list(result))

result = map(lambda x: ('성인' if x['age'] > 20 else '청소년'), people)
print(list(result))

result = filter(lambda x: x['age'] > 20, people)
print(list(result))



def cal2(a, b=3):
    return a + 2 * b

print(cal2(4))
print(cal2(4, 2))
print(cal2(a=6))
print(cal2(a=1, b=7))



def call_names(*args):
    for name in args:
        print(f'{name}야 밥먹어라~')

call_names('철수','영수','희재')


def get_kwargs(**kwargs):
    print(kwargs)

get_kwargs(name='bob')
get_kwargs(name='john', age='27', height=180)



class Monster():
    hp = 100
    alive = True

    def damage(self, attack):
        self.hp = self.hp - attack
        if self.hp < 0:
            self.alive = False

    def status_check(self):
        if self.alive:
            print('살아있다')
        else:
            print('죽었다')

m = Monster()
m.damage(120)

m2 = Monster()
m2.damage(90)

m.status_check()
m2.status_check()



