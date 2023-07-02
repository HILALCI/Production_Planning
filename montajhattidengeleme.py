import numpy as np
import pandas as pd
import math

uretims = int(input("Lutfen kac saat uretim yapilcagini giriniz: "))
kuretim = int(input("Lutfen kac tane uretilmesi gerektigini giriniz: "))
isoge = int(input("Lutfen kac tane is ogesi old. giriniz: "))

liste = list()

for i in range(isoge):
    x = int(input(f"Lutfen {i+1}. is ogesinin islem suresini giriniz: "))
    liste.append(x)

liste = np.array(liste)

toplam = liste.sum()

T = uretims * 60
US = kuretim
C = T/US

print("Toplam = ",toplam)
print("T = ", T)
print("C = ", C)

nenk = toplam / C
nenk = math.ceil(nenk)
nolasi = len(liste[liste > (C/2)])

print("nenk = ", nenk)
print(liste[liste > (C/2)], "nolasi= ",nolasi)

nenaz= max(nenk, nolasi)

print("nenaz = ",nenaz)

n=9

D = ((((n*C) - toplam) / (n*C)) * 100)
DI = ((math.sqrt((sum(liste.max() - liste)**2)) / (n*C)) * 100)
HE = (toplam / (n*C)) * 100
KE = (toplam / (nenaz * C)) * 100


print("D = %", D)
print("DI = %", DI)
print("HE = %", HE)
print("KE = %", KE)

if (HE == KE):
    print("En yuksek hat etkinligine ulasilmistir.")