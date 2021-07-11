# Yazılar
print("merhaba dünya")

x = 5
print(type(x))

x = 7.8
print(type(x)) #zaten int ve float ları gördük.

x = "hello" 
print(type(x))

x = 'hello'
print(type(x))

# Gelelim '' ve "" olayına. Mantıklı olan "" kullanmak. Çünkü 'Kco'nun Yeri' hata verir ama "Kco'nun Yeri" hata vermez. Ama diğer durumlarda '' da kullanılabilir. Yani "" ile '' işaretleri arasında fark yok.

'''
 'Kco'nun Yeri'
  File "<ipython-input-6-7e714a04de49>", line 1
    'Kco'nun Yeri'
         ^
SyntaxError: invalid syntax
'''

print("Kco'nun Yeri")

# Cevaplar

ab = 3,15 
c = 2

print(ab * c)

# python , işaretini başka bir değer olarak görüyor yani 3,15 i 3 ve 15 değerleri, 3.15 i 3 tam yüzde 15 olarak görüyor.


yas = input("Yaşınızı giriniz ")

print(yas * 3)

print(type(yas))

# Python 60 sayısını yazı olarak alıyor. Peki biz yazıyı sayıya çevirebilir miyiz? Evet


sayı_yas = int(yas)

print(type(sayı_yas))

print(sayı_yas * 3)

soyad = "Nsisc"

print(len(soyad)) #len() karakter uzunluğunu yazdırır

print("hello python")

# Peki biz hello yazdıktan sonra python kelimesini bir satır aşağıya yazabilir miyiz? Evet.


print("hello \npython") #/n next anlamına geliyor ve bu bir satır aşağıya iniyor.

isimler = input("Adınızı giriniz ")

print(isimler[2])

print(isimler[7])

print(isimler[5])

# Neler oluyorrr. Biz ismi verdikten sonra bunu isimler değişkenine kaydetti. Biz köşeli parantez içine yazdığımız sayıncı indexteki karakteri aldı. İndex ilk karakterden başlayarak 0,1,2,3,4,... diye sayılır.Peki neden isimler[5] dediğimde boşluk geldi? Çünkü 5. index boşluk karakteri. Hesaplayalım, "B"(0), "e"(1), "y"(2), "z"(3), "a"(4), " "(5)


print(isimler[-2])

# Bu sefer sondan geriye 2. olan karakteri aldı.


print(isimler[0] + " " + isimler[-1])

# Bankalarda olan ilk ve son harfi alma bu şekilde yapılabilir.


yeniyazi = "abcdefgh"

print(yeniyazi[5])

print(yeniyazi[2:])

# 2. indexten başlayarak sona kadar aldı.

print(yeniyazi[:3])

# 3. indexe kadar (3. indexi almadan) aldı sonra bitirdi.

gelenveri = "Ahmedinyasi35"

print(gelenveri[-2:])

# Sondan ikinciyi dahil ederek aldı

print(gelenveri[2:5])

# Burada başlayıp bitireceği yeri söyledik o da uyguladı. Yeni bir şey yok.


print(gelenveri[::2])

# Burada 2 tane iki nokta koydukan sonra sayı yazarsak atlama miktarı oluyor. Her iki karakterden birini alıyor. Yani bir alıyor bir almıyor bir alıyor bir almıyor...


print(gelenveri[2:12:3])

# Dedim ki 2. indexten başla 12. indexe kadar git (12. dahil değil) ama karakterleri 3-3-3 al dedim.


print(gelenveri[::-1])


# Burada da sondan başa 1,1 aldı. Yani yazı ters döndü.

# Yazı Metodları

ad = "kco"

print(ad.capitalize())



print(ad)

# capitilize()ilk harfi büyütür. Ama değeri değiştirmez. Biz istersek capitalize edilmiş halini bir değişkene kaydedip kullanabiliriz


Benimtamadım = "Kco Nsisc"

print(Benimtamadım.split())

# split() boşluk olan yerlerden stringleri ayırır.


print(Benimtamadım.upper())


# upper() bütün harfleri büyütür.


a = "merhaba"
b = "benim"
c = "adım"
d = "kco"
e = " "
f = d.capitalize()

print(a + e + b + e + c + e + f)



print(a * 4)

# Python galiba delirmiş. Yazıları birbiriyle topladı ve çarptı. Bu diğer dillerde olmayan bir özellik. Python yazıları topladığında yan yana getiriyor, çarptığında yazıyı çarptığı sayı kadar yan yana yazıyor.