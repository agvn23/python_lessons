# ═══════════════════════════════════════════════════════════════
# PALINDROME CHECK
# Palindrom: Baştan ve sondan aynı okunan kelime
# Örnekler: "racecar", "madam", "kayak"
# ═══════════════════════════════════════════════════════════════

# Yöntem 1: Slicing
def is_palindrome_v1(s):
    """
    .lower() → Tüm harfleri küçük yapar (büyük-küçük harf duyarsız)
    .replace(" ", "") → Boşlukları kaldırır
    s == s[::-1] → Orijinal ile tersi aynı mı?
    """
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Yöntem 2: Two Pointer
def is_palindrome_v2(s):
    """
    İki pointer: Baştan ve sondan ortaya doğru ilerle.
    Her adımda karakterleri karşılaştır.
    Eğer farklı bir çift bulursan → Palindrom değil.
    """
    s = s.lower().replace(" ", "")
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False      # Eşleşmeyen çift → Palindrom değil
        left += 1
        right -= 1
    
    return True               # Tüm çiftler eşleşti → Palindrom

# TEST
print(is_palindrome_v1("racecar"))      # True
print(is_palindrome_v1("hello"))        # False
print(is_palindrome_v2("A man a plan a canal Panama"))  # True