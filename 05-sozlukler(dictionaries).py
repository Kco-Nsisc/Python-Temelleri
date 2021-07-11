# Sözlükler
# Sözlükleri bir anahtar-değer ilişkisine benzetebilirsiniz. Anahtarı veriyorsunuz değeri alıyorsunuz gibi. Hadi şimdi örneklere bakalım.


benimsozluk = {"elma" : 100 , "karpuz" : 200 , "muz" : 300}

print(benimsozluk["elma"]) # [elma] burada anahtar oluyor karşılığında 100 yani değer geliyor.

print(benimsozluk["muz"])

print(type(benimsozluk))


benimsozluk["elma"] = 500

print(benimsozluk)

# Az önce de dediğimiz gibi sözlük yapıları şu şekilde çalışır: key : value (anahtar : değer). Mesela karpuz kelimesi anahtar 200 de değer. Aynı internet şifreleri gibi düşünebilirsiniz. Şifreyi(key) giriyorsunuz ve hesabınıza giriyorsunuz(value). Eğer şifre(key) yanlışsa siz hesaba(value) giremezsiniz.

# Sözlüklerin Özellikleri
# Sözlük yapısında veriler değiştirlebiliyor.


degisik = {"anah1" : 10000 , "anah2" : [1,5,2,778,"kco"] , "anah3" : {"anah4" : "kase"}}

kasevalue = degisik["anah3"]["anah4"]

print(kasevalue)

kcovalue = degisik["anah2"][4]

print(kcovalue)

print(degisik)

degisik["anah2"][3] = 7

print(degisik)

# 778 değeri 7 oldu

degisik.pop("anah1")

print(degisik)

# pop() verilen anahtarı ve anahtarın sahip olduğu değeri siler.