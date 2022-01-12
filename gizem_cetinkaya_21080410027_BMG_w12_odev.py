#isimler, cinsiyet, matematik, türkçe listelerinden oluşan sinav_sonuc adında sözlük oluşturma
sinav_sonuc = {'isimler':['ayse k.','ahmet m.','nuri c.','nawwar t.','suzan t.','ala b.'],
'cinsiyet':['k','e','e','e','k','k'],
'matematik':[60,40,97,45,56,95],
'türkce':[70,30,23,80,78,46]}
kız_sayısı=0
erkek_sayısı=0
kız_matematik=0
erkek_matematik=0
kız_türkce_not=0
erkek_türkce_not=0
kız_türkçe_listesi=[]
erkek_türkçe_listesi=[]

#Matematik dersinin ortalamasını kadınlar ve erkekler için hesaplama ve Türkçe dersinin sınıf ortalamasını ekrana yazdırma
for x in range (len(sinav_sonuc['cinsiyet'])): #uzunluk
    if sinav_sonuc['cinsiyet'][x]=='k':
        kız_sayısı+=1
        kız_matematik= kız_matematik + sinav_sonuc['matematik'][x]
        kız_türkce_not= kız_türkce_not + sinav_sonuc['türkce'][x]
        kız_türkçe_listesi.append(sinav_sonuc['türkce'][x])
    else :
        erkek_sayısı+=1
        erkek_matematik = erkek_matematik + sinav_sonuc ['matematik'][x]
        erkek_türkce_not = erkek_türkce_not + sinav_sonuc ['türkce'][x]
        erkek_türkçe_listesi.append(sinav_sonuc ['türkce'][x])

print(f"kadınların matematik not ortalaması: {kız_matematik / kız_sayısı}\n\
erkeklerin matematik not ortalaması:{erkek_matematik / erkek_sayısı}\n\
türkçe dersinin sinif not ortalması :{(kız_türkce_not + erkek_türkce_not)/(erkek_sayısı + kız_sayısı)}")

#Kadınların en yüksek Türkçe notunu ve erkeklerin en yüksek Türkçe notunu ekrana yazdırma
print(f"kadınlar arasında en yüksek türkçe not:{max(kız_türkçe_listesi)}")
print(f"erkekler arasında en yüksek türkçe not:{max(erkek_türkçe_listesi)}")