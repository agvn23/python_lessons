╔══════════════════════════════════════════════════════════════════════╗
║                    PYTHON FONKSİYON REHBERİ                        ║
╠══════════════════╦═══════════════════════════════════════════════════╣
║                  ║                                                   ║
║  GENEL           ║  print()     → Ekrana yazdırır                   ║
║  FONKSİYONLAR    ║  len()       → Uzunluk (list, str, dict...)      ║
║                  ║  type()      → Veri tipini döner                  ║
║                  ║  range()     → Sayı dizisi üretir                 ║
║                  ║  enumerate() → (index, değer) çifti üretir        ║
║                  ║  max()       → En büyük değer                     ║
║                  ║  min()       → En küçük değer                     ║
║                  ║  sum()       → Toplam                             ║
║                  ║  abs()       → Mutlak değer                       ║
║                  ║  sorted()    → Sıralı kopya döner                 ║
║                  ║  int()       → Tam sayıya çevir                   ║
║                  ║  str()       → String'e çevir                     ║
║                  ║  float()     → Ondalıklı sayıya çevir             ║
║                  ║  input()     → Kullanıcıdan girdi al              ║
║                  ║  isinstance()→ Tip kontrolü                       ║
╠══════════════════╬═══════════════════════════════════════════════════╣
║                  ║                                                   ║
║  LİSTE           ║  .append(x)  → Sona ekle                         ║
║  METOTLARI       ║  .insert(i,x)→ i. indexe ekle                    ║
║                  ║  .remove(x)  → İlk x'i sil                       ║
║                  ║  .pop(i)     → i. indexten çıkar (varsayılan: son)║
║                  ║  .sort()     → Yerinde sırala                     ║
║                  ║  .reverse()  → Yerinde tersine çevir              ║
║                  ║  .index(x)   → x'in indexini bul                  ║
║                  ║  .count(x)   → x kaç kez var?                     ║
║                  ║  .extend(lst)→ Başka listeyi ekle                 ║
║                  ║  .copy()     → Kopya oluştur                      ║
╠══════════════════╬═══════════════════════════════════════════════════╣
║                  ║                                                   ║
║  STRİNG          ║  .lower()    → Tümünü küçük harf                  ║
║  METOTLARI       ║  .upper()    → Tümünü büyük harf                  ║
║                  ║  .strip()    → Baş/son boşlukları sil             ║
║                  ║  .split(sep) → Ayırarak listeye çevir              ║
║                  ║  .join(lst)  → Listeyi birleştirerek string yap    ║
║                  ║  .replace(a,b)→ a'yı b ile değiştir               ║
║                  ║  .find(x)    → x'in indexini bul (-1 yoksa)       ║
║                  ║  .startswith()→ ... ile başlıyor mu?              ║
║                  ║  .endswith() → ... ile bitiyor mu?                ║
║                  ║  .isdigit()  → Tümü rakam mı?                     ║
║                  ║  .isalpha()  → Tümü harf mi?                      ║
╠══════════════════╬═══════════════════════════════════════════════════╣
║                  ║                                                   ║
║  SÖZLÜK          ║  .get(key, default) → Güvenli erişim              ║
║  METOTLARI       ║  .keys()     → Tüm anahtarlar                    ║
║                  ║  .values()   → Tüm değerler                      ║
║                  ║  .items()    → (anahtar, değer) çiftleri          ║
║                  ║  .update(d2) → Başka dict ile güncelle             ║
║                  ║  .pop(key)   → Anahtarı sil ve değerini döndür    ║
╠══════════════════╬═══════════════════════════════════════════════════╣
║                  ║                                                   ║
║  SET             ║  .add(x)     → Eleman ekle                        ║
║  METOTLARI       ║  .remove(x)  → Eleman sil (yoksa hata)           ║
║                  ║  .discard(x) → Eleman sil (yoksa hata yok)       ║
║                  ║  .union(s2)  → Birleşim (| operatörü)             ║
║                  ║  .intersection(s2) → Kesişim (& operatörü)        ║
║                  ║  .difference(s2)   → Fark (- operatörü)           ║
╚══════════════════╩═══════════════════════════════════════════════════╝