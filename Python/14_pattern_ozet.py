# ═══════════════════════════════════════════════════════════════
# PATTERN 1: Hash Map ile Sayma / Arama
# Ne zaman kullan: "Daha önce gördük mü?" soruları
# Örnekler: Two Sum, Contains Duplicate, First Unique Character
# ═══════════════════════════════════════════════════════════════
# seen = {}
# for item in collection:
#     if item in seen:        ← O(1) arama
#         # İşlem yap
#     seen[item] = value

# ═══════════════════════════════════════════════════════════════
# PATTERN 2: Stack ile Eşleştirme
# Ne zaman kullan: İç içe yapılar, parantez eşleştirme
# Örnekler: Valid Parentheses, Min Stack
# ═══════════════════════════════════════════════════════════════
# stack = []
# for item in collection:
#     if koşul:
#         stack.append(item)   ← push
#     else:
#         stack.pop()          ← pop

# ═══════════════════════════════════════════════════════════════
# PATTERN 3: Two Pointer (İki İşaretçi)
# Ne zaman kullan: Sıralı dizilerde çift arama, palindrom
# Örnekler: Reverse String, Palindrome, Two Sum (sorted)
# ═══════════════════════════════════════════════════════════════
# left = 0
# right = len(arr) - 1
# while left < right:
#     # Karşılaştır, ilerlet

# ═══════════════════════════════════════════════════════════════
# PATTERN 4: Set ile Filtreleme
# Ne zaman kullan: "Var mı / yok mu?" kontrolü, benzersizlik
# Örnekler: Destination City, Contains Duplicate
# ═══════════════════════════════════════════════════════════════
# lookup = set(collection)
# for item in other_collection:
#     if item not in lookup:   ← O(1) arama
#         # İşlem yap

# ═══════════════════════════════════════════════════════════════
# PATTERN 5: Queue ile Simülasyon
# Ne zaman kullan: Sıra takibi, seviye seviye işleme (BFS)
# Örnekler: Time to Buy Tickets, BFS traversal
# ═══════════════════════════════════════════════════════════════
# from collections import deque
# queue = deque(initial_items)
# while queue:
#     current = queue.popleft()
#     # İşlem yap
#     # Gerekirse queue.append(new_item)