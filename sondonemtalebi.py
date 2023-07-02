"""
Son Dönem Talebi Yöntemi
▪ Bir önceki dönemde gerçekleşmiş talebi, gelecek dönemde de gerçekleşecek talebin tahmini olarak kullanan yöntemdir
"""
gercek_satis = [6000, 4000, 8000, 7000, 4000, 7000, 6000, 8000, 9000, 10000, 12000, 13000]
hata = 0

for i in range(len(gercek_satis)):
    if (i == 0):
        print("Gercek   Tahmin   Sapma(Hata)\n---------------------")
        print(gercek_satis[i],"-","-",sep="\t")
    else:
        print(gercek_satis[i], gercek_satis[i-1], abs(gercek_satis[i] - gercek_satis[i-1]), sep="\t")
        hata += abs(gercek_satis[i] - gercek_satis[i-1])

print("  Topam Hata = ", hata)