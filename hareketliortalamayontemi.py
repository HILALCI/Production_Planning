"""
Hareketli Ortalama Yöntemi
Gelecek dönemin talebi önceki n dönemde gerçeklemiş talebin ortalaması alınarak bulunur.

Dt* : t. dönem için tahmini talep değeri(hareketli ortalama)
Dt-i : t. dönemden i dönem öncesinin gerçekleşen talebi
n : hareketli ortalamada göz önüne alınacak dönem sayısı

        n
Dt* = E         = Dt-i / n
        i =1

"""

n = int(input("Lutfen tam sayi giriniz: "))

gercek_satis = [6000, 4000, 8000, 7000, 4000, 7000, 6000, 8000, 9000, 10000, 12000, 13000]

gercek_degerler, hata, pivot = 0, 0, 0


print("Gercek   Tahmin   Sapma(Hata)\n---------------------")
for i in range(len(gercek_satis)):
    if (i < n):
        print(gercek_satis[i],"-","-",sep="\t")
    
    else:
        gercek_degerler = gercek_satis[pivot:i]
        print(gercek_satis[i],sum(gercek_degerler)/n, abs(gercek_satis[i] - sum(gercek_degerler)/n), sep="\t")
        hata += abs(gercek_satis[i] - sum(gercek_degerler)/n)
        pivot += 1

print("  Topam Hata = ", hata)