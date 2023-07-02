"""
Korelasyon analizi: Bu analizde geleceğe ilişkin değeri tahmin edilmek istenen değişkenle, onu etkileyen değişken veya 
değişkenler arasındaki ilişkinin derecesi araştırılır. İlişkinin derecesi r ile ölçülür
"""

"""
Korelasyon katsayıları için su ilişki ve ifadeler yazılabilir
−1 ≤ 𝑟 ≤ 1
𝑟 < 0 𝑖𝑠𝑒 𝑋 𝑣𝑒 𝑌 arasında ters yönlü ilişki vardır. Yani X artarken Y azalır veya X azalırken Y 
artar
0,9 ≤ 𝑟 ≤ 1 𝑖𝑠𝑒 𝑋 𝑣𝑒 𝑌 𝑎𝑟𝑎𝑠𝑖𝑛𝑑𝑎 𝑐𝑜𝑘 𝑠ı𝑘ı 𝑏𝑖𝑟 𝑖𝑙𝑖𝑠𝑘𝑖 𝑣𝑎𝑟𝑑𝑖𝑟
0,7 ≤ 𝑟 < 0,9 𝑖𝑠𝑒 𝑋 𝑣𝑒 𝑌 𝑎𝑟𝑎𝑠𝑖𝑛𝑑𝑎 𝑠ı𝑘ı 𝑖𝑙𝑖𝑠𝑘𝑖 𝑣𝑎𝑟𝑑𝑖𝑟
0,4 ≤ 𝑟 < 0,7 𝑖𝑠𝑒 𝑋 𝑣𝑒 𝑌 𝑎𝑟𝑎𝑠𝑖𝑛𝑑𝑎 𝑜𝑟𝑡𝑎 𝑑𝑒𝑟𝑒𝑐𝑒𝑙𝑖 𝑖𝑙𝑖𝑠𝑘𝑖 𝑣𝑎𝑟𝑑𝑖𝑟
0,2 ≤ 𝑟 < 0,4 𝑖𝑠𝑒 𝑋 𝑣𝑒 𝑌 𝑎𝑟𝑎𝑠𝑖𝑛𝑑𝑎 𝑧𝑎𝑦𝑖𝑓 𝑖𝑙𝑖𝑠𝑘𝑖 𝑣𝑎𝑟𝑑𝑖𝑟
0 ≤ 𝑟 < 0,2 𝑖𝑠𝑒 𝑋 𝑣𝑒 𝑌 𝑎𝑟𝑎𝑠𝑖𝑛𝑑𝑎 𝑐𝑜𝑘 𝑧𝑎𝑦𝑖𝑓 𝑖𝑙𝑖𝑠𝑘𝑖 𝑣𝑎𝑟𝑑𝑖r
"""

import math

x = [1,2,3,4,5,6,7,8,9,10,11,12]
y = [6,4,8,7,4,7,6,8,9,10,12,13]

xkar2 = list(map(lambda x: x**2 ,x))
ykar2 = list(map(lambda y: y**2 ,y))
xy = list(map(lambda x,y: x*y ,x,y))

n = len(x)

r = (sum(xy) - (sum(x) * sum(y) / n)) / (math.sqrt((sum(xkar2) - (sum(x) ** 2 / n)) * (sum(ykar2) - (sum(y) ** 2 / n))))

print("r = ",r)

if r <= 0.2:
    print("𝑋 𝑣𝑒 𝑌 𝑎𝑟𝑎𝑠ı𝑛𝑑𝑎 𝑐𝑜𝑘 𝑧𝑎𝑦𝑖𝑓 𝑖𝑙𝑖𝑠𝑘𝑖 𝑣𝑎𝑟𝑑ı𝑟.")
elif r <= 0.4:
    print("𝑋 𝑣𝑒 𝑌 𝑎𝑟𝑎𝑠ı𝑛𝑑𝑎 𝑧𝑎𝑦𝑖𝑓 𝑖𝑙𝑖𝑠𝑘𝑖 𝑣𝑎𝑟𝑑ı𝑟.")
elif r <= 0.7:
    print("𝑋 𝑣𝑒 𝑌 𝑎𝑟𝑎𝑠ı𝑛𝑑𝑎 𝑜𝑟𝑡𝑎 𝑑𝑒𝑟𝑒𝑐𝑒𝑙𝑖 𝑖𝑙𝑖𝑠𝑘𝑖 𝑣𝑎𝑟𝑑ı𝑟.")
elif r <= 0.9:
    print("𝑋 𝑣𝑒 𝑌 𝑎𝑟𝑎𝑠ı𝑛𝑑𝑎 𝑠ı𝑘ı 𝑖𝑙𝑖𝑠𝑘𝑖 𝑣𝑎𝑟𝑑ı𝑟.")
else:
    print("𝑋 𝑣𝑒 𝑌 𝑎𝑟𝑎𝑠ı𝑛𝑑𝑎 𝑐𝑜𝑘 𝑠ı𝑘ı 𝑏𝑖𝑟 𝑖𝑙𝑖𝑠𝑘𝑖 𝑣𝑎𝑟𝑑ı𝑟.")