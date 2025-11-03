import random as rd
s=[]
cows=0
bulls=0
for i in range(0,4):
    k=rd.randint(0,9)
    s.append(str(k))
k=''.join(s)
m=list(input('enter the four digit number'))
for i in range(0,4):
    if s[i]==m[i]:
        cows+=1
    else:
        bulls+=1
print(f'the cows score is {cows} and bulls score is {bulls}')
if cows>bulls:
    print(f"cows has higher score {cows} and cows wins!!!!")
elif cows==bulls:
    print('your both scores are equal')
else:
    print(f'the bulls score is higher {bulls},bulls win!!!!!!')


print(s)
print(m)