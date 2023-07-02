"""
Gelecek dönem tahmini= Bir önceki dönem tahmini + Düzeltme Katsayısı x Tahmin Hatası
D*(t+1) = D*t + a(Dt - D*t)
 D*(t+1) = D*t + (1- a)D*t

 Dt : t. donem gerceklesen satis degeri
 D*t: t. donem icin hesaplanan tahmin talep degeri
 a(alfa): 0<a<1 arasinda deger alir.Genelde 0.2 ile 0.8 arasinda secilmesi onerilmektedir.

"""
import numpy as np

n = int(input("Lutfen tam sayi giriniz(n): "))
a = float(input("Lutfen 0<a<1 giriniz(alfa): "))
pivot,hata = 0,0
tahminler = list()

gercek_satis = np.array([6000, 4000, 8000, 7000, 4000, 7000, 6000, 8000, 9000, 10000, 12000, 13000])


print("Gercek   Tahmin   Sapma(Hata)\n---------------------")
for i in range(len(gercek_satis)):
    if (i < n):
        print(gercek_satis[i],"-","-",sep="\t")
    
    else:
        if(i == n):
            tahmin = sum(gercek_satis[0:i]) / n
            tahminler.append(tahmin)
            j = 0
        else:
            tahmin = (tahminler[j] + (a*(gercek_satis[i-1] - tahminler[j])))
            tahminler.append(tahmin)
            j+=1
        
        print(gercek_satis[i],tahmin, abs(gercek_satis[i] - tahmin), sep="\t")
        hata += abs(gercek_satis[i] - tahmin)
        pivot += 1

print("  Topam Hata = ", hata)
