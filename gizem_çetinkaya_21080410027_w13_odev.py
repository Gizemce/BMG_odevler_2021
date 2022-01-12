

#sinav_sonuc adli sozluk olusturma.
sinav_sonuc = {'isimler':[ ' emir a. ',' ali b. ' ,' seda c. ' , ' gulcan d. ',' rabia e.','busra .'],
'cinsiyet':['e','e','k','k','k','k'],
'matematik':['65 , 30 , 77 , 45 , 59 , 85'],
'turkce':['48 , 50 , 73 , 94 , 87 , 40'],
}
#Kullanicinin  girdigi bilgileri sinav_sonuc adli sozluge ekleyen fonksiyon.
def ogrenci_bilgileri_guncelleme(isim,cinsiyeti,matematiknot,turkce):
   sinav_sonuc['isimler'].append(isim)
   sinav_sonuc['cinsiyet'].append(cinsiyeti)
   sinav_sonuc['matematik'].append(matematiknot)
   sinav_sonuc['turkce'].append(turkce)

#Kullanicidan 2 yeni kayit girmesini isteme.
isim_1=input('1.ogrencinin ismini"isim soyismin_ilk_harfi." olarak giriniz:')
cinsiyet_1=input("ogrencinin cinsiyeti erkek ise e Kiz ise k harfini giriniz:")
matematik_1=input("ogrencinin matematik dersinden aldigi notu giriniz:")
Turkce_1=input("ogrencinin Turkce dersinden aldigi notu giriniz:")

ogrenci_bilgileri_guncelleme(isim_1,cinsiyet_1,matematik_1,Turkce_1)


isim_2=input('2. ogrencinin ismini"isim soyismin_ilk_harfi." olarak giriniz:')
cinsiyet_2=input("ogrencinin cinsiyeti erkek ise e Kiz ise k harfini giriniz.")
matematik_2=input("ogrencinin matematik dersinden aldigi notu giriniz:")
Turkce_2=input("ogrencinin Turkce dersinden aldigi notu giriniz:")

ogrenci_bilgileri_guncelleme(isim_2,cinsiyet_2,matematik_2,Turkce_2)


#Girilen yeni kayitlarla birlikte guncellenmis olan tabloyu (sinav_sonuc sozlugunu) ekrana yazdirma.
print(sinav_sonuc)

#listeyi duzgun yazarsak eger.
print("isimler:",sinav_sonuc['isimler'])
print("Cinsiyetleri (e olanlar erkek, kiz olanlar k harfiyle gosterilmistir.):",sinav_sonuc['cinsiyet'])
print("Matematik derslerinden alinan notlar:",sinav_sonuc['matematik'])
print("Turkce dersinden alinan notlar:",sinav_sonuc['turkce'])

