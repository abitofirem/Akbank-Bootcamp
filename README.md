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
# ... istasyon eklemeleri
rota = metro.en_az_aktarma_bul("M1", "K4")
```

## Görselleştirme

Metro ağı, her hattın farklı renklerle görselleştirildiği ve her bağlantındaki mesafelerin etiketlendiği şekilde sunulmuştur. Kullanıcılar, metro ağını görsel olarak inceleyebilir, istasyonlar arasındaki bağlantıları ve süreleri kolayca görebilirler. Aşağıda, metro ağını gösteren görsel örneği bulunmaktadır:

![Image](https://github.com/user-attachments/assets/c9bd0f1b-ea61-42d8-9456-1bbf5b28cf63)

### Graf Görselleştirme Detayları

- **Ağ Görselleştirme**: NetworkX kütüphanesi ile oluşturulan graf, her bir istasyon (düğüm) ve bağlantı (kenar) için renkli gösterimler kullanır.
- **Renkler**: Farklı hatlar, farklı renklerde gösterilmektedir. Örneğin, kırmızı hat, mavi hat, yeşil hat gibi renklerle tanımlanmış olup görselde bu renkler açıkça ayırt edilebilir.
- **Bağlantı Mesafeleri**: Bağlantı üzerindeki süreler, kenar etiketleri olarak gösterilmiştir, böylece kullanıcılar her bir yolun ne kadar süre aldığını kolayca görebilir.

## Kurulum

Metro ağını görselleştirebilmek ve çalıştırabilmek için gerekli kütüphaneleri yüklemek için aşağıdaki komutları kullanabilirsiniz:

```bash
pip install networkx matplotlib
```

## Kullanıcı Arayüzü (GUI) Eklemek

Görselleştirmeyi daha kullanıcı dostu hale getirmek için bir GUI eklenmesi faydalı olabilir. Bu GUI, kullanıcıların başlangıç ve hedef istasyonlarını seçebileceği, ardından en az aktarmalı ve en hızlı rotayı görsel olarak görebileceği bir arayüz olabilir.

## Projenin Gelecekteki Gelişimi

- **Dinamik Veri Entegrasyonu**: Metro hattı ve istasyonları için gerçek zamanlı veri entegrasyonu eklenebilir.
- **Mobil Uygulama**: Proje, bir mobil uygulamaya dönüştürülerek kullanıcıya sunulabilir.
- **Daha Karmaşık Metro Ağı Modelleri**: Daha büyük şehirlerin verileriyle genişletilebilir.
- **Kullanıcı Geri Bildirim Sistemi**: Kullanıcıların rotaları değerlendirebileceği sistemler eklenebilir.

## Geliştirme Fikirleri

- Farklı Rotasyon Yöntemleri: A* algoritmasına ek olarak Dijkstra, Bellman-Ford gibi yöntemler eklenebilir.
- Gerçek Zamanlı Trafik ve Kapasite Bilgisi: Metro istasyonlarındaki doluluk oranları, anlık trafik durumu gibi bilgiler rota hesaplamasında kullanılabilir.

---

## 📂 Projeyi Çalıştırmak

```bash
git clone https://github.com/abitofirem/Akbank-Bootcamp.git
cd Akbank-Bootcamp
python AdSoyad_MetroSimulation.py
```

---

## ✨ Yazar

**İrem Yalçın**  
[GitHub](https://github.com/abitofirem)
