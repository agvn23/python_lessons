# ═══════════════════════════════════════════════════════════════
# VALID PARENTHESES - Stack Çözümü
# Zaman Karmaşıklığı: O(n) → String'i bir kez geziyoruz
# Alan Karmaşıklığı:  O(n) → En kötü durumda tüm karakterler stack'e girer
# ═══════════════════════════════════════════════════════════════

def is_valid(s):
    """
    Algoritma:
    ─────────
    1. Bir sözlük oluştur: kapatan → açan eşleştirmesi
    2. String'deki her karakter için:
       - Açan parantezse → Stack'e koy (push)
       - Kapatan parantezse → Stack'in tepesine bak:
         - Stack boşsa → Eşleşecek açan yok → False
         - Tepedeki açan uygun değilse → Yanlış eşleşme → False
         - Tepedeki açan uygunsa → Stack'ten çıkar (pop) → Devam
    3. Sonunda stack boşsa → True, değilse → False
    
    Kullanılan Fonksiyonlar:
    ───────────────────────
    - dict{}  : Sözlük oluşturma → Kapatan-Açan eşleştirmesi için
    - list[]  : Stack olarak kullanılır (.append ve .pop ile)
    - "in"    : Bir anahtarın sözlükte olup olmadığını kontrol eder
    - .append(): Stack'in tepesine eleman ekler (push)
    - .pop()  : Stack'in tepesinden eleman çıkarır (pop)
    - len()   : Stack'in uzunluğunu kontrol eder
    """
    
    # Kapatan → Açan eşleştirmesi
    # Neden bu yön? Çünkü stringde kapatan parantez gördüğümüzde
    # "bunun açanı ne?" diye sormamız gerekiyor
    bracket_map = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    
    # Stack: açan parantezleri burada tutacağız
    stack = []
    
    for char in s:           # String'deki her karakter üzerinde gez
        if char in bracket_map:   # Bu bir KAPATAN parantez mi?
            # Stack boşsa veya tepedeki eşleşmiyorsa → Geçersiz
            if not stack or stack[-1] != bracket_map[char]:
                # not stack → Stack boş mu kontrolü
                #   Boş stack "falsy"dir, not ile True olur
                # stack[-1] → Stack'in tepesi (son eleman)
                # bracket_map[char] → Bu kapatanın açanı ne olmalı?
                return False
            stack.pop()     # Eşleşme başarılı → Açanı stack'ten çıkar
        else:
            stack.append(char)   # AÇAN parantez → Stack'e ekle
    
    # Stack boş olmalı → Tüm açanlar eşleşmiş demektir
    # len(stack) == 0 ile aynı şey: not stack
    return len(stack) == 0

# TEST
print(is_valid("()"))        # True
print(is_valid("()[]{}"))    # True
print(is_valid("(]"))        # False
print(is_valid("([])"))      # True
print(is_valid("("))         # False → Açan var ama kapatan yok
print(is_valid(")"))         # False → Stack boş, kapatan geldi

# ═══════════════════════════════════════════════════════════════
# TRACE (İz Sürme) - "([])" örneği:
# ─────────────────────────────────
# char="("  → Açan → stack: ["("]
# char="["  → Açan → stack: ["(", "["]
# char="]"  → Kapatan → bracket_map["]"]="[" 
#              → stack[-1]="[" == "[" ✓ → pop → stack: ["("]
# char=")"  → Kapatan → bracket_map[")"]="("
#              → stack[-1]="(" == "(" ✓ → pop → stack: []
# Döngü bitti → stack boş → return True ✓
# ═══════════════════════════════════════════════════════════════