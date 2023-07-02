talep = [450,600,475,475]

donem_sonu_stok = 500
donem_basi_stok = 500

stok = ((donem_sonu_stok - donem_basi_stok) / len(talep)) + donem_basi_stok

stoklar = list()
stoklar.append(int(stok))
for i in range(len(talep)):
    stok = ((donem_sonu_stok - donem_basi_stok) / len(talep)) + stoklar[i]
    stoklar.append(int(stok))

uretim = list()

for i in range(1,len(talep)+1):
    uretim.append(talep[i-1]+ (stoklar[i] - stoklar[i-1]))

print("Uretim\tTalep\tDonem Sonu Stok")
for i in range(len(talep)):
    print(uretim[i], talep[i], stoklar[i], sep="\t")  
