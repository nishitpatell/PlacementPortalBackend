#lambda -> anonymous function

from functools import reduce


def square(x):
    return x*x

res = square(5)
print(res)

res1 = lambda x: x*x
print(res1(5))

f2 = lambda x,y: x+y    
print(f2(5,6))

nums = [1,2,3,4,5]

evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

doubleevens = list(map(lambda x: x*2, evens))
print (doubleevens)

sum = reduce(lambda x,y: x+y, doubleevens)
print(sum)