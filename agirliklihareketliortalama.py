"""
Ağırlıklı Hareketli Ortalama Yöntemi
Bu yöntemin özelliği, Ağırlıklı Ortalama Yönteminde olduğu gibi dönemleri ağırlıklandırması; ancak geçmiş tüm değerleri değil, belli sayıdaki en yakın dönem değerleri göz önüne alınır.

         n
D*t=     E       Wi*D(t-i)
         i = 1

D*t: tahmin talep değeri (Ağırlıklı ortalama)
D(t-i) : i. dönem  için gerçekleşen talep değeri
Wi : i. dönem gerçekeleşen talep değerinin tahmine etkisi (i. donem ağırlık katsayısı)
n : agirlikli hareketli ortalamada goz onune alinacak donem sayisi

Ayrıca su koşullar söz konusudur.
0 < Wi < 1 (i = 1,2,...,n)
 n
E       = Wi = 1
 i = 1
"""
import numpy as np

n = int(input("Lutfen tam sayi giriniz(n): "))
agirliklar = list()
pivot,hata = 0,0

for i in range(1,n+1):
    w = int(input(f"Lutfen {i}. agirlik degerini giriniz: "))
    agirliklar.append(w)

agirliklar = np.array(agirliklar)
gercek_satis = np.array([6000, 4000, 8000, 7000, 4000, 7000, 6000, 8000, 9000, 10000, 12000, 13000])


print("Gercek   Tahmin   Sapma(Hata)\n---------------------")
for i in range(len(gercek_satis)):
    if (i < n):
        print(gercek_satis[i],"-","-",sep="\t")
    
    else:
        gercek_degerler = gercek_satis[pivot:i]
        tahmin = sum((gercek_degerler * agirliklar) /100)
        print(gercek_satis[i],tahmin, abs(gercek_satis[i] - tahmin), sep="\t")
        hata += abs(gercek_satis[i] - tahmin)
        pivot += 1

print("  Topam Hata = ", hata)