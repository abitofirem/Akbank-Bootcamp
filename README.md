# 🚇 Sürücüsüz Metro Simülasyonu (Rota Optimizasyonu)

Bu proje, iki metro istasyonu arasında:
- **En az aktarmalı rotayı** (BFS algoritması ile)
- **En hızlı rotayı** (A* algoritması ile)  
bulan bir simülasyon geliştirmeyi amaçlamaktadır.

---

## 🧠 Kullanılan Teknolojiler ve Kütüphaneler

- `Python 3.10+`
- `collections.deque` → BFS için kuyruk yapısı
- `heapq` → A* için öncelik kuyruğu
- `typing` → Tip ipuçları ve anlaşılır fonksiyonlar için

---

## 🔍 Algoritmaların Açıklaması

### 🔹 BFS (Breadth-First Search)
- Amaç: **En az aktarma sayısıyla** hedefe ulaşmak
- Her istasyon, komşularına sırayla bakar
- Kuyruk sistemiyle ilk bulunan hedef döndürülür

### 🔹 A* (A Star)
- Amaç: **Toplam geçiş süresi en az olan** rotayı bulmak
- Her komşuya geçiş süresi eklenerek en kısa süreli yol aranır
- `heapq` ile en ucuz yol her zaman öne alınır

---

## 📌 Örnek Test Senaryoları

```
1. AŞTİ → OSB
   En az aktarma: AŞTİ → Kızılay → Ulus → OSB
   En hızlı rota:  AŞTİ → Kızılay → Ulus → OSB (25 dk)

2. Keçiören → AŞTİ
   En az aktarma: Keçiören → Gar → Kızılay → AŞTİ
   En hızlı rota:  Keçiören → Gar → Kızılay → AŞTİ (19 dk)
```

---

## 💡 Geliştirme Fikirleri

- Metro ağını **görselleştirme** (networkx + matplotlib)
- JSON dosyasından istasyon yükleme
- Web arayüzü (Flask)
- Kullanıcıdan canlı istasyon seçimi (input)

---

## 📂 Kurulum

```bash
git clone https://github.com/abitofirem/Akbank-Bootcamp.git
cd Akbank-Bootcamp
python AdSoyad_MetroSimulation.py
```

---

## ✨ Yazar

**İrem Yalçın**  
[GitHub Profilin](https://github.com/abitofirem)
