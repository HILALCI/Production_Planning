"""
Yıllık Parasal Hacim = Yıllık Talep * Birim Maliyet

Source : Üretim ve Operasyon Yönetimi 26 ABC Analizi, İsmail Başoğlu, https://www.youtube.com/watch?v=Na4hDKT1Q2o
"""

yillik_talep = [2000,1550,1200,1000,1000,600,500,350,250,100]

birim_maliyet = [0.60,17.00,0.42,12.50,90.00,14.17,154.00,42.86,0.60,8.50]
yph = list()


for i in range(len(birim_maliyet)):
    yph.append(yillik_talep[i]*birim_maliyet[i])

sortedyph = yph.copy()
sortedyph.sort(reverse=True)

a = int(20  * len(birim_maliyet) / 100)
b = int(30  * len(birim_maliyet) / 100)
c = int(50  * len(birim_maliyet) / 100)
iter = 0


print("Yillik Talep\tBirim Maliyet\tYillik Parasal Hacim(YPH)\tABC Sinifi")
for i in sortedyph:
    if iter < a:
        abc = "A"
    elif iter-a < b:
        abc = "B"
    else: #else yapsakta olur sanırım ama iter-b < c bu sekildede cikiyor.
        abc = "C"
    
    geti = yph.index(i)
    print(yillik_talep[geti],"", birim_maliyet[geti],"", yph[geti],"\t\t",abc, sep="\t")

    iter += 1






