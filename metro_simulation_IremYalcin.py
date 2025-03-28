from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional
import networkx as nx
import matplotlib.pyplot as plt




class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ıarı

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if idx not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)

    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        queue = deque([(baslangic, [baslangic])])
        ziyaret_edildi = set()

        while queue:
            mevcut, rota = queue.popleft()

            if mevcut.idx == hedef.idx:
                return rota

            ziyaret_edildi.add(mevcut.idx)

            for komsu, _ in mevcut.komsular:
                if komsu.idx not in ziyaret_edildi:
                    queue.append((komsu, rota + [komsu]))

        return None

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        pq = [(0, id(baslangic), baslangic, [baslangic])]
        ziyaret_edildi = set()

        while pq:
            sure, _, mevcut, rota = heapq.heappop(pq)

            if mevcut.idx == hedef.idx:
                return (rota, sure)

            if mevcut.idx in ziyaret_edildi:
                continue
            ziyaret_edildi.add(mevcut.idx)

            for komsu, gecis_suresi in mevcut.komsular:
                if komsu.idx not in ziyaret_edildi:
                    toplam_sure = sure + gecis_suresi
                    heapq.heappush(pq, (toplam_sure, id(komsu), komsu, rota + [komsu]))

        return None
    
    
#Görselleştirme fonksiyonu
def metro_agini_gorsellestir(metro):
    G = nx.Graph()  # Yeni bir grafik nesnesi oluşturuyoruz.

    #Hattın renklerini belirliyoruz
    hat_renkleri = {
        "Kırmızı Hat": "red",
        "Mavi Hat": "blue",
        "Turuncu Hat": "orange",
        "Yeşil Hat": "green",
        "Mor Hat": "purple"
    }

    #İstasyonlar ve bağlantılar ekleme
    for istasyon_id, istasyon in metro.istasyonlar.items():
        hat_renk = hat_renkleri.get(istasyon.hat, "gray")  # Varsayılan renk: gri
        G.add_node(istasyon.ad, color=hat_renk)  # İstasyonu grafiğe ekliyoruz

        for komsu, sure in istasyon.komsular:
            G.add_edge(istasyon.ad, komsu.ad, weight=sure)  # Bağlantıları ekliyoruz

    #Grafik özellikleri
    pos = nx.spring_layout(G)  # Düğümlerin konumlarını belirliyoruz

    #Düğüm renklerini, her hattın rengine göre ayarlıyoruz
    node_colors = [G.nodes[node]['color'] for node in G.nodes]

    #Çizim: Nokta ve bağlantı renklerini özelleştiriyoruz
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=3000, font_size=10, font_weight="bold", edge_color="black", width=2)

    #Bağlantı ağırlıklarını etiket olarak alıyoruz
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8, font_color="red")

    #Başlık ve grafik gösterimi
    plt.title("Metro Ağı Görselleştirme")
    plt.show()


    
    
#Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()

    #İstasyonlar ekleme
    
    #Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")

    #Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")

    #Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")
    
    #Yeşil Hat
    metro.istasyon_ekle("Y1", "Gazi", "Yeşil Hat")
    metro.istasyon_ekle("Y2", "Emek", "Yeşil Hat")
    metro.istasyon_ekle("Y3", "Bahçelievler", "Yeşil Hat")
    metro.istasyon_ekle("Y4", "Kolej", "Yeşil Hat")

    #Mor Hat
    metro.istasyon_ekle("P1", "OSTİM", "Mor Hat")
    metro.istasyon_ekle("P2", "Gimat", "Mor Hat")
    metro.istasyon_ekle("P3", "AŞTİ", "Mor Hat")  #AŞTİ zaten var, aktarma olacak


    metro.baglanti_ekle("K1", "K2", 4)
    metro.baglanti_ekle("K2", "K3", 6)
    metro.baglanti_ekle("K3", "K4", 8)
    metro.baglanti_ekle("M1", "M2", 5)
    metro.baglanti_ekle("M2", "M3", 3)
    metro.baglanti_ekle("M3", "M4", 4)
    metro.baglanti_ekle("T1", "T2", 7)
    metro.baglanti_ekle("T2", "T3", 9)
    metro.baglanti_ekle("T3", "T4", 5)
    metro.baglanti_ekle("K1", "M2", 2)
    metro.baglanti_ekle("K3", "T2", 3)
    metro.baglanti_ekle("M4", "T3", 2)
    
    # Yeni Eklediğim Yeşil Hat bağlantıları
    metro.baglanti_ekle("Y1", "Y2", 4)  #Gazi -> Emek
    metro.baglanti_ekle("Y2", "Y3", 3)  #Emek -> Bahçelievler
    metro.baglanti_ekle("Y3", "Y4", 2)  #Bahçelievler -> Kolej

    #Aktarma bağlantısı
    metro.baglanti_ekle("Y4", "K1", 2)  #Kolej (Yeşil Hat) ↔ Kızılay (Kırmızı Hat)

    #Mor Hat bağlantıları
    metro.baglanti_ekle("P1", "P2", 5)  # OSTİM -> Gimat
    metro.baglanti_ekle("P2", "P3", 6)  # Gimat -> AŞTİ

    #AŞTİ aktarması (Mor ↔ Mavi)
    metro.baglanti_ekle("P3", "M1", 1)  #AŞTİ (Mor) ↔ AŞTİ (Mavi)

    print("\n=== Test Senaryoları ===")

    def yazdir(rota):
        onceki = None
        output = []
        for istasyon in rota:
            if onceki is None or onceki.ad != istasyon.ad:
                output.append(istasyon.ad)
            onceki = istasyon
        print(" -> ".join(output) + " -> SON")

    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:")
        yazdir(rota)

    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):")
        yazdir(rota)

    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:")
        yazdir(rota)

    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):")
        yazdir(rota)

    print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:")
        yazdir(rota)

    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):")
        yazdir(rota)
        
    
    print("\n4. Gazi'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("Y1", "K4")
    if rota:
        print("En az aktarmalı rota:", end=" ")
        yazdir(rota)

    sonuc = metro.en_hizli_rota_bul("Y1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", end=" ")
        yazdir(rota)

    print("\n4. OSTİM'den Keçiören'e:")
    rota = metro.en_az_aktarma_bul("P1", "T4")
    if rota:
        print("En az aktarmalı rota:", end=" ")
        yazdir(rota)

    sonuc = metro.en_hizli_rota_bul("P1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", end=" ")
        yazdir(rota)


    metro_agini_gorsellestir(metro)
