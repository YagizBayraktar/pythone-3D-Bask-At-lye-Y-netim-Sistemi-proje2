from veri_islemleri import verileri_yukle


def rapor_baslik():
    print("+" + "-" * 52 + "+")
    print("|" + "RAPORLAMA EKRANI".center(52) + "|")
    print("+" + "-" * 52 + "+")


def istatistik_goster():
    veriler = verileri_yukle()
    rapor_baslik()
    print("\n> GENEL ISTATISTIKLER")
    print("-" * 54)

    if not veriler:
        print("Henuz kayit olmadigi icin istatistik hesaplanamiyor.")
        return

    toplam_proje = len(veriler)
    toplam_gram = sum(kayit["gram"] for kayit in veriler)
    toplam_sure = sum(kayit["sure"] for kayit in veriler)
    toplam_maliyet = sum(kayit["maliyet"] for kayit in veriler)

    tamamlanan = sum(1 for kayit in veriler if kayit["durum"].lower() == "tamamlandi")
    basilan = sum(1 for kayit in veriler if kayit["durum"].lower() == "basiliyor")
    hazirlanan = sum(1 for kayit in veriler if kayit["durum"].lower() == "hazirlaniyor")

    ortalama_maliyet = toplam_maliyet / toplam_proje
    ortalama_gram = toplam_gram / toplam_proje

    print(f"Toplam proje sayisi        : {toplam_proje}")
    print(f"Toplam filament kullanimi  : {toplam_gram:.2f} gram")
    print(f"Toplam baski suresi        : {toplam_sure:.2f} saat")
    print(f"Toplam maliyet             : {toplam_maliyet:.2f} TL")
    print(f"Ortalama proje maliyeti    : {ortalama_maliyet:.2f} TL")
    print(f"Ortalama filament kullanimi: {ortalama_gram:.2f} gram")
    print(f"Hazirlanan proje sayisi    : {hazirlanan}")
    print(f"Basiliyor proje sayisi     : {basilan}")
    print(f"Tamamlanan proje sayisi    : {tamamlanan}")


def yuksek_tuketim_goster():
    veriler = verileri_yukle()
    rapor_baslik()
    print("\n> YUKSEK TUKETIM RAPORU")
    print("-" * 54)

    if not veriler:
        print("Henuz kayit yok.")
        return

    yuksekler = [kayit for kayit in veriler if kayit["gram"] >= 500]

    if not yuksekler:
        print("500 gram ve ustu filament kullanan proje bulunamadi.")
        return

    print("500 gram ve ustu filament kullanan projeler:\n")
    for kayit in yuksekler:
        print(
            f"ID: {kayit['id']} | "
            f"Model: {kayit['model_adi']} | "
            f"Filament: {kayit['filament_turu']} | "
            f"Gram: {kayit['gram']} g | "
            f"Maliyet: {kayit['maliyet']} TL"
        )


def filament_analizi_goster():
    veriler = verileri_yukle()
    rapor_baslik()
    print("\n> FILAMENT ANALIZI")
    print("-" * 54)

    if not veriler:
        print("Henuz kayit yok.")
        return

    toplamlar = {"PLA": 0, "ABS": 0, "PETG": 0}

    for kayit in veriler:
        filament = kayit["filament_turu"].upper()
        if filament in toplamlar:
            toplamlar[filament] += kayit["gram"]

    print("Filament turlerine gore toplam kullanim:\n")
    for filament, gram in toplamlar.items():
        print(f"{filament}: {gram:.2f} gram")