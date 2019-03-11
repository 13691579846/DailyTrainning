num = int(input('请输入一个数：'))
l=list(range(1, int((1+num)*num/2+1)))[::-1]
print(l)
for i in range(num):
    print(' '*(2*num-((i+1)*2)),end='')# 13,10,7,4,1
    for k in range(i+1):
        if len(l) !=0:
            print(l.pop(),end='')
        print(end=' ')

    print()

def func(num):
    if num ==1:
        return 1
    return func(num-1)+num

n = func(num)

