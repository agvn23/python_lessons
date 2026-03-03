# ═══════════════════════════════════════════════════════════════
# REVERSE STRING - Birden Fazla Yöntem
# ═══════════════════════════════════════════════════════════════

# Yöntem 1: Slicing (En Pythonic)
def reverse_v1(s):
    """
    s[::-1] → String slicing
    [start:stop:step]
    start = başlangıç (boş = baştan)
    stop  = bitiş (boş = sona kadar)
    step  = adım (-1 = geriye doğru)
    """
    return s[::-1]

# Yöntem 2: Döngü ile (Algoritmayı anlamak için)
def reverse_v2(s):
    """Her karakteri ters sıraya ekle."""
    result = ""
    for char in s:
        result = char + result   # Yeni karakteri BAŞA ekle
    return result

# Yöntem 3: Two Pointer (İki İşaretçi) - Liste üzerinde in-place
def reverse_v3(s_list):
    """
    İki pointer: biri başta, biri sonda → Ortada buluşana kadar yer değiştir.
    
    ['h','e','l','l','o']
     L               R    → swap → ['o','e','l','l','h']
         L       R         → swap → ['o','l','l','e','h']
             LR            → L >= R → DUR
    """
    left = 0
    right = len(s_list) - 1
    
    while left < right:
        # Python'da swap: a, b = b, a
        s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1
    
    return s_list

# TEST
print(reverse_v1("hello"))                    # "olleh"
print(reverse_v2("hello"))                    # "olleh"
print(reverse_v3(['h','e','l','l','o']))      # ['o','l','l','e','h']