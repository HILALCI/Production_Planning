"""
Eğilim bazlı teknik: Regresyon analizi
▪ Regresyon analizi; geçmiş verilerin tümünü dikkate alarak eğilim doğrusunun/egrisinin hesaplanmasına ve bu 
doğru aracılığıyla tahminde bulunulmasına olanak veren bir yöntemdir.
▪ Bu analizde, geleceğe ilişkin değeri öngörülmek istenen değişken(talep) ile, bu değişkeni etkileyen bir değişken 
(donem numarası) arasındaki ilişkinin matematiksel olarak ifade edilir.

            𝑌 = 𝑎 + 𝑏𝑋

Doğrusal regresyon formülü aşağıdaki gibi ifade edilir.
Denklemdeki a ve b parametreleri su şekilde hesaplanır.


a = E y - b * E x / n

b =  n * E x * y - (Ex * Ey) / n *Ex^2 - (Ex)^2  


"""

x = [1,2,3,4,5,6,7,8,9,10,11,12]
y = [6,4,8,7,4,7,6,8,9,10,12,13]


xkar2 = list(map(lambda x: x**2 ,x))
xy = list(map(lambda x,y: x*y ,x,y))

n = len(x)
b = ( n * sum(xy) - ( sum(x) * sum(y) ) ) / ( n * sum(xkar2) - pow(sum(x), 2) )

a = (sum(y) / 12) - (b  * sum(x) / n)


print("X\tY\ty\t\t\tHata")
for i in range(n):
    Y = a + b * x[i]

    print(x[i], y[i], Y, abs(Y-y[i]), sep="\t")


print("\n=========")
print("a = ", a)
print("b = ", b)