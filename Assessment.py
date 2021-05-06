a = {6,7,8,9,10} 
b = {5,6,7,8,9}
a.add(4)
print(a)
b.add(3)
print(b)
print (a.union(b))
print(a.difference(b))
print(a.intersection(b))

lst=[11, 100, 99, 1000, 999,99]
lst[0]=-1
print(lst)
print(lst[0])
print(lst[5])
lst.count(99)
print(lst)
print(sum(lst))
print(min(lst))

years=(2020,2070)
for year in years:
    if year%4==0:
        print(year)

numbers=range(1000,2000)
for number in numbers:
    if number%7==0 and number%5!=0:
        print(number)

nums=range(1,11)
for num in nums:
    print(num)

odd_nums=range(30,50)   
for o in odd_nums:
    if o%2!=0:
        print(o)

x=[]
Numbers=range(100,200)
for n in Numbers:
    if n%7==0:
        x.append(n)

print(x)


digits=range(1,50)

for d in digits:
    if d%3==0 and d%5==0:
        print("purple white")
    if d%3==0:
        print("Purple")
    if d%5==0:
       print("white")


