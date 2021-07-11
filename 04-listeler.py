# Listeler
# Biz şu ana kadar verilerimizi (sayılar, yazılar) değişkenlerde saklamayı öğrendik. Ama şöyle bir sıkıntı var. Biz 20 veri saklayacaksak 20 ayrı değişken oluştururuz. Bu da kodun karışmasına sebep olur. Bunun yerine listeleri kullanacağız.


yazı = "cem kerem"
'''
yazı[1] = "a" # [1] demek yazı değişkeninin 1. karakteridir. Aman dikkat yazılarda, listelerde vb. karakter saymaya 0 dan başlarız. Bu durumda yazı değişkenindeki 0. karaket c 1. karakter e oluyor.
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-2-f5fb97695916> in <module>
----> 1 yazı[1] = "a" #[1] demek yazı değişkeninin 1. karakteridir. Aman dikkat yazılarda, listelerde vb. karakter saymaya 0 dan başlarız. Bu durumda yazı değişkenindeki 0. karaket c 1. karakter e oluyor.

TypeError: 'str' object does not support item assignment
'''
# Biz yazıların belirli bir karakterini değiştiremeyiz. Ama listelerin belirli bir karakterini değiştirebiliriz. Mesela,


benimlistem = [10,20,30,40]
# Aslında noktanın virgülle farkı burada daha iyi anlaşılır. Nokta virgüllü sayıların kesirli yeri ile tam sayı yerini ayırırken, virgül ise değerleri ayırırken kullanılır.


print(benimlistem[3])

# Burada benimlistem' deki 3. karakter (0 dan saymaya başladığımızı unutmayın bu çok önemli) 40 oluyor.


benimlistem[3] = 50

print(benimlistem)

# Burada 3. karakteri yani 40 ı 50 yaptık yazılar bu kodla değişmez ama listeler değişir.


numa = 1
numb = 20

numlar = [numa, numb]
# Listelere veri olarak değişkenleri de girebiliriz.

print(numlar)

print(benimlistem)


benimlistem.append(99)
# append() içine girilen veriyi listenin sonuna ekler.


print(benimlistem)

# Liste Metodları

yeniListe = ["a","a","a","a","a","a","b","b","b","c","c","c",3,4,5,6,7,7,77,2,"g"]

yeniListe.append("u")

print(yeniListe)

yeniListe.pop()

# pop() son karakteri siler.


print(yeniListe)

yeniListe.remove("a")
# remove() söylenen karakteri çıkarır


print(yeniListe)

print(yeniListe.count("a"))

# count() verilen karakterin kaç adet olduğunu gösterir


aliste = ["h","j","k","l","ş","i"]

print(aliste * 3)


aba = [3,4,5,6,7,8,9,0]

aba.reverse()

print(aba)

# reverse() listeyi ters çevirir.

# Karmaşık Liste Olayları

listee = [1,3,5,"Kco",89,"Nsisc"]

print(type(listee))

sonucum = listee[3]
print(sonucum)

print(type(sonucum))

dogruli = [0,3,6,"kim",[5,"aslı","z"]]

print(type(dogruli[4]))


print(dogruli[4])


zdegiskeni = dogruli[4][2]

print(zdegiskeni)

# dogruli[4][2] demek dogruli listesinin 4. elemanının 2. elemanını al. Hadi şimdi listede belirtilen yeri yazdırmaya çalışalım.


karmasikliste = ["a",[877,47,"djkf","838",[884,["g",["hadi yazdır burayı"]]]]]

asonucum = karmasikliste[1][4][1][1]

print(asonucum)
