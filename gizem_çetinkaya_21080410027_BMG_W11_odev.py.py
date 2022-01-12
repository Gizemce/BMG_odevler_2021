kisiler=[]

X=input("str(X) GİR:")
print(X)

Y=input("str(Y) GİR:")
print(Y)


Z=input("str(Z) GİR:")
print(Z)

T=input("str(T) GİR:")
print(T)

#X,Y,Z,T değerlerini kisiler listesine tanımla
print("kisiler listesini ekrana yaz:")
kisiler = [X , Y , Z ,T]
print(kisiler)


#listenin uzunluğu nedir
print("listenin uzunlugu nedir:")
print(len(kisiler))



#listenin son elemanını siliniz
print("listenin son elemanını sil:")
kisiler.pop(3)
print(kisiler)

#kisiler listesini tekrar yazdır
print("kisiler listesini tekrar yazdır:")
kisiler = [X , Y , Z ,T]
print(kisiler)
