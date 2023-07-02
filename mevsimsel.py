"""

"""


x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
y = [1,3,4,2,1,3,5,3,2,4,6,3,2,5,7,4]


xkar2 = list(map(lambda x: x**2 ,x))
xy = list(map(lambda x,y: x*y ,x,y))

n = len(x)
b = ( n * sum(xy) - ( sum(x) * sum(y) ) ) / ( n * sum(xkar2) - pow(sum(x), 2) )

a = (sum(y) - (b *sum(x))) / n
 
print("X\tY\ty\t\t\tHata\t\t\ty/Y")
for i in range(n):
    Y = a + b * x[i]

    print(x[i], y[i], Y, abs(Y-y[i]),y[i]/Y, sep="\t")