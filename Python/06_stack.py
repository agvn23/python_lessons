# --- STACK (YIĞIN) ---
# Düşün: Üst üste konmuş tabaklar → En son koyduğunu ilk alırsın
# Python'da list ile stack yapılır

#  TEMEL İŞLEMLER:
#  push → .append()   → Üste ekle
#  pop  → .pop()      → Üstten çıkar
#  peek → stack[-1]   → Üsttekine bak (çıkarmadan)

stack = []

# Push (ekleme)
stack.append("A")
stack.append("B")
stack.append("C")
print(stack)         # ["A", "B", "C"]  → C en üstte

# Peek (üsttekine bakma)
print(stack[-1])     # "C"

# Pop (çıkarma)
print(stack.pop())   # "C" → Son eklenen ilk çıkar
print(stack)         # ["A", "B"]

# Boş mu kontrolü
print(len(stack) == 0)  # False
# veya
print(not stack)        # False (boş liste falsy'dir)