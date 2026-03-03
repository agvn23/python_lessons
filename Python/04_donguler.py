# --- FOR DÖNGÜSÜ ---
# Bir koleksiyondaki (liste, string, range...) her eleman üzerinde tek tek gezer

# range(n) → 0'dan n-1'e kadar sayı üretir
for i in range(5):
    print(i)       # 0, 1, 2, 3, 4

# range(start, stop) → start'tan stop-1'e kadar
for i in range(2, 6):
    print(i)       # 2, 3, 4, 5

# range(start, stop, step) → adım adım
for i in range(0, 10, 2):
    print(i)       # 0, 2, 4, 6, 8

# Liste üzerinde gezme
sehirler = ["Istanbul", "Ankara", "Izmir"]
for sehir in sehirler:
    print(sehir)

# enumerate() → Hem index hem değeri verir
for index, sehir in enumerate(sehirler):
    print(f"Index {index}: {sehir}")
    # Index 0: Istanbul
    # Index 1: Ankara
    # Index 2: Izmir

# --- WHILE DÖNGÜSÜ ---
# Koşul True olduğu sürece çalışır
sayac = 0
while sayac < 5:
    print(sayac)    # 0, 1, 2, 3, 4
    sayac += 1      # sayac = sayac + 1

# --- break ve continue ---
# break    → Döngüyü tamamen durdurur
# continue → O adımı atlar, sonraki adıma geçer

for i in range(10):
    if i == 3:
        continue    # 3'ü atla
    if i == 7:
        break       # 7'de dur
    print(i)        # 0, 1, 2, 4, 5, 6