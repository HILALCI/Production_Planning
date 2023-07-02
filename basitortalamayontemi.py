"""
Basit Ortalama Yöntemi
Basit ortalama yöntemi bir serideki veriler toplamının, fiili gözlem sayısına bölünmesi yoluyla bulunur. 
Gelecek için büyük bir değişiklik beklenmiyorsa, bu yöntem kullanılabilir.
"""

gercek_satis = [6000, 4000, 8000, 7000, 4000, 7000, 6000, 8000, 9000, 10000, 12000, 13000]

gercek, hata = 0, 0

for i in range(len(gercek_satis)):
    if (i == 0):
        print("Gercek   Tahmin   Sapma(Hata)\n---------------------")
        print(gercek_satis[i],"-","-",sep="\t")
        gercek +=  gercek_satis[i]
    
    else:
        print(gercek_satis[i], gercek/i, abs(gercek_satis[i] - (gercek/i)), sep="\t")
        gercek += gercek_satis[i]
        hata += abs(gercek_satis[i] - (gercek/i))

print("  Topam Hata = ", hata)