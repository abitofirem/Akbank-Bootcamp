# 🚇 Sürücüsüz Metro Simülasyonu (Rota Optimizasyonu)


Bu proje, bir şehirdeki metro ağı üzerinde iki istasyon arasındaki en az aktarmalı ve en hızlı rotaları bulan bir simülasyon sistemini içermektedir. BFS (Breadth-First Search) ve A* algoritmalarını kullanarak metro istasyonları arasındaki bağlantıları analiz eder ve kullanıcılara farklı rotaları sunar.

## Kullanılan Teknolojiler ve Kütüphaneler

- **Python**: Projenin ana dili.
- **NetworkX**: Graf veri yapısını yönetmek ve görselleştirme yapmak için kullanılır.
- **Matplotlib**: Grafiği görselleştirmek için kullanılır.

## Algoritmaların Çalışma Mantığı

### BFS (Breadth-First Search) Algoritması
BFS algoritması, bir kaynaktan başlayarak en kısa yolu bulmak için kullanılan bir arama algoritmasıdır. Bu algoritma, en az aktarmalı rotayı bulmak için kullanılır. Kuyruk (queue) yapısı kullanarak istasyonlar arasında en kısa yolun belirlenmesi sağlanır.

### A* Algoritması
A* algoritması, her adımda bir "f" değeri hesaplar. Bu değerin minimum olmasını sağlayarak, kaynaktan hedefe en hızlı yolu bulur. Hem gerçek maliyeti hem de hedefe olan tahmini mesafeyi dikkate alır.

## Hatlar ve Renkler

Aşağıdaki hatlar ve renkler kullanılarak metro ağı görselleştirilmiştir:

- **Kırmızı Hat**: Kızılay -> Ulus -> Demetevler -> OSB (Mesafeler: Kızılay -> Ulus: 4 dk, Ulus -> Demetevler: 6 dk, Demetevler -> OSB: 8 dk)
- **Mavi Hat**: AŞTİ -> Kızılay -> Sıhhiye -> Gar (Mesafeler: AŞTİ -> Kızılay: 5 dk, Kızılay -> Sıhhiye: 3 dk, Sıhhiye -> Gar: 4 dk)
- **Turuncu Hat**: Batıkent -> Demetevler -> Gar -> Keçiören (Mesafeler: Batıkent -> Demetevler: 7 dk, Demetevler -> Gar: 9 dk, Gar -> Keçiören: 5 dk)
- **Yeşil Hat**: Gazi -> Emek -> Bahçelievler -> Kolej (Mesafeler: Gazi -> Emek: 4 dk, Emek -> Bahçelievler: 3 dk, Bahçelievler -> Kolej: 2 dk)
- **Mor Hat**: OSTİM -> Gimat -> AŞTİ (Mesafeler: OSTİM -> Gimat: 5 dk, Gimat -> AŞTİ: 6 dk)

## Test Senaryoları ve Örnek Kullanım

1. **AŞTİ'den OSB'ye**
   - En az aktarmalı rota ve en hızlı rota hesaplanır.
   
2. **Batıkent'ten Keçiören'e**
   - Aynı şekilde, en az aktarmalı ve en hızlı rota hesaplanır.
   
3. **Keçiören'den AŞTİ'ye**
   - Yine benzer şekilde hesaplama yapılır.

4. **Gazi'den OSB'ye**
   - Gazi istasyonundan OSB'ye olan en az aktarmalı ve en hızlı rota hesaplanır.

### Örnek Kullanım:

```python
metro = MetroAgi()

# İstasyonlar ekleme
metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
# ... (Diğer istasyon eklemeleri ve bağlantılar)

# Test senaryosu
rota = metro.en_az_aktarma_bul("M1", "K4")
if rota:
    print("En az aktarmalı rota:")
    yazdir(rota)

sonuc = metro.en_hizli_rota_bul("M1", "K4")
if sonuc:
    rota, sure = sonuc
    print(f"En hızlı rota ({sure} dakika):")
    yazdir(rota)


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
[GitHub](https://github.com/abitofirem)
