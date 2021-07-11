# Setler
# Setler listelerle aynıdır. Sadece listelerde olduğu gibi bir veri birden fazla olamaz.

benimList = ["a","b","kr",5,6,8,9,9,"a"]

print(benimList)

benimListSet = set(benimList)

print(benimListSet)

# Burada da aynı verilerden 1 tane olabildiğini daha iyi anlamış olduk.

benimset = {"a","a", 5,5,6,7,7,"6","6",6}
# Eee hani değerler birtane olurdu hata vermedi. benimset' in değerlerine bakalım.


print(benimset)

benimset.add("b")

print(benimset)

# Seti Boş Yapma (Sana demedim yanlış anlama :D)

bosliste = []
print(bosliste)
print(type(bosliste))


bosset = {}
print(bosset)
print(type(bosset))

# Eee buna boş sözlük dedi nasıl set yapcaz? Böyle.


benimbossetim = set()

print(type(benimbossetim))

benimbossetim.add(1000)

print(benimbossetim)

# Buraya kadar geldiysen tebrikler. Hiç durmadan yola devam.