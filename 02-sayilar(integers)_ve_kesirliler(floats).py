# Operatöler
# Matematikteki işlemler python'da bazı işaretlerle tanımlanmıştır. Bunlar; Toplama + Çıkarma - Çarpma * Bölme / Mod % Mod nedir? Mod (x % y) bir sayının (x) diğer bir sayıya (y) bölümünden kalan sayıdır. Bölüm demedim kalan dedim.

# İnt ve Float

a = 20 # değişkenleri zaten biliyoruz
b = 10

print(a / b) #20 / 10
print(type(a / b)) # type() bize içinde yazılan şeyin hangi türe ait olduğunu gösterir.


# float demek kersirli, ondalık sayı; int(eger) = tam sayı demektir.


print(a * b) #20 * 10
print(type(a * b))



# Neden böyle oldu? Yani bölmede sonuç tam sayı olmasına rağmen neden kesirli verdi de çarpmada tam sayı olarak verdi? Python şöyle düşünüyor: 5/3 ondalıklı çıkıyor ama 6/3 tam sayı çıkıyor. Sonuçları tam sayılı gösterirsem hata olur çünkü 5/3 1 den fazla 2 den az. Ben en iyisi sadece bölme işleminde sonucu ondalıklı olarak göstereyim. İsteyen kodla beraber sonucu tam sayı yapsın. ( 5//2 = 2 ama 5/2 = 2,5)


print(5/2)

print(5//2)



pi = 3.14
b = 2

print(pi * b)


ab = 3,15
c = 2

print(ab * c)


# Neden böyle oldu? Sonuçta ab = 3 tam yüzde on beş değil mi? Cevabı yazılar kısmında :)

# Matematiksel İşlemler

x = 4
y = 5

print(x * y * 10)



print(x * x * x * x * x * x * x)

# Peki ben böyle tek tek sayıları yazmak zorunda mıyım? Tabii ki hayır. x x x x x x x = x 7 ( üs alma)

print(x ** 7)



print(100 % 2)

print(101 % 2)


# Tekrar hatırlatmakta fayda var. % = mod alma yani sağdaki sayıyı soldakine bitene kadar böler. Tek mi çift mi belirlenirken kullanılabilir.


yas = input("Yaşınızı giriniz ") # input() fonksiyonunu kullanıcıdan değer girmesini istediğimizde kullanırız.


print(yas * 3)


# Neden 606060 yazdırdı dersen cevabı yazılar kısmında :)