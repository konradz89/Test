def generator(x,y):
while x<y:
yield x
x += 1
ilosc_linijek = input()
i = 0
while(i < int(ilosc_linijek)):
v=eval(input())
x = v[0]
y = v[1]
z = sum(generator(x,y))
print(z)
i += 1