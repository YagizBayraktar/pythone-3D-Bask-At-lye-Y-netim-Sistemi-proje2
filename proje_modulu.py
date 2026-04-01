from datetime import datetime
from veri_islemleri import verileri_yukle, verileri_kaydet, yeni_id_uret


def baslik_yaz():
    print("+" + "-" * 52 + "+")
    print("|" + "3D BASKI ATOLYE YONETIM SISTEMI".center(52) + "|")
    print("+" + "-" * 52 + "+")


def alt_baslik_yaz(metin):
    print("\n> " + metin)
    print("-" * 54)


def kayit_yazdir(kayit):
    print("-" * 54)
    print(f"ID                : {kayit['id']}")
    print(f"Model Adi         : {kayit['model_adi']}")
    print(f"Kategori          : {kayit['kategori']}")
    print(f"Filament Turu     : {kayit['filament_turu']}")
    print(f"Renk              : {kayit['renk']}")
    print(f"Kullanilan Gram   : {kayit['gram']} g")
    print(f"Baski Suresi      : {kayit['sure']} saat")
    print(f"Hesaplanan Maliyet: {kayit['maliyet']} TL")
    print(f"Durum             : {kayit['durum']}")
    print(f"Not               : {kayit['not']}")
    print(f"Kayit Tarihi      : {kayit['tarih']}")


def sayi_al(mesaj):
    while True:
        veri = input(mesaj).strip().replace(",", ".")
        try:
            sayi = float(veri)
            if sayi < 0:
                print("Negatif deger girilemez.")
                continue
            return sayi
        except ValueError:
            print("Hatali giris yaptin. Sayisal deger gir.")


def durum_al():
    durumlar = ["hazirlaniyor", "basiliyor", "tamamlandi"]
    while True:
        durum = input("Durum (Hazirlaniyor/Basiliyor/Tamamlandi): ").strip().lower()
        if durum in durumlar:
            return durum.title()
        print("Gecerli durumlar: Hazirlaniyor, Basiliyor, Tamamlandi")


def filament_al():
    gecerli_filamentler = ["PLA", "ABS", "PETG"]
    while True:
        filament = input("Filament turu (PLA/ABS/PETG): ").strip().upper()
        if filament in gecerli_filamentler:
            return filament
        print("Gecerli filament turleri: PLA, ABS, PETG")


def maliyet_hesapla(gram, filament_turu):
    fiyatlar = {
        "PLA": 500,
        "ABS": 560,
        "PETG": 430
    }

    filament_turu = filament_turu.upper()

    if filament_turu not in fiyatlar:
        filament_turu = "PLA"

    kg_fiyat = fiyatlar[filament_turu]
    maliyet = (gram / 1000) * kg_fiyat
    return round(maliyet, 2)


def proje_ekle():
    veriler = verileri_yukle()
    baslik_yaz()
    alt_baslik_yaz("YENI PROJE EKLE")

    model_adi = input("Model adi: ").strip().title()
    kategori = input("Kategori (dekor, oyuncak, yedek parca vb.): ").strip().title()
    filament_turu = filament_al()
    renk = input("Renk: ").strip().title()
    gram = sayi_al("Kullanilan filament miktari (gram): ")
    sure = sayi_al("Baski suresi (saat): ")
    durum = durum_al()
    not_alani = input("Kisa not: ").strip()

    maliyet = maliyet_hesapla(gram, filament_turu)

    kayit = {
        "id": yeni_id_uret(veriler),
        "model_adi": model_adi,
        "kategori": kategori,
        "filament_turu": filament_turu,
        "renk": renk,
        "gram": gram,
        "sure": sure,
        "maliyet": maliyet,
        "durum": durum,
        "not": not_alani,
        "tarih": datetime.now().strftime("%d.%m.%Y %H:%M")
    }

    veriler.append(kayit)
    verileri_kaydet(veriler)

    print("\nKayit basariyla eklendi.")
    print(f"Hesaplanan maliyet: {maliyet} TL")


def projeleri_listele():
    veriler = verileri_yukle()
    baslik_yaz()
    alt_baslik_yaz("TUM PROJELER")

    if not veriler:
        print("Henuz kayit bulunmuyor.")
        return

    for kayit in veriler:
        kayit_yazdir(kayit)


def proje_ara():
    veriler = verileri_yukle()
    baslik_yaz()
    alt_baslik_yaz("PROJE ARA")

    if not veriler:
        print("Aranacak kayit bulunmuyor.")
        return

    aranacak = input("Model adi, kategori, filament, renk veya durum gir: ").strip().lower()

    bulunanlar = []
    for kayit in veriler:
        metin = (
            f"{kayit['model_adi']} "
            f"{kayit['kategori']} "
            f"{kayit['filament_turu']} "
            f"{kayit['renk']} "
            f"{kayit['durum']}"
        ).lower()

        if aranacak in metin:
            bulunanlar.append(kayit)

    if not bulunanlar:
        print("Sonuc bulunamadi.")
        return

    print(f"\n{len(bulunanlar)} kayit bulundu:")
    for kayit in bulunanlar:
        kayit_yazdir(kayit)


def id_ile_kayit_bul(veriler, kayit_id):
    for kayit in veriler:
        if kayit["id"] == kayit_id:
            return kayit
    return None


def proje_duzenle():
    veriler = verileri_yukle()
    baslik_yaz()
    alt_baslik_yaz("PROJE DUZENLE")

    if not veriler:
        print("Duzenlenecek kayit bulunmuyor.")
        return

    try:
        kayit_id = int(input("Duzenlenecek proje ID: "))
    except ValueError:
        print("Gecersiz ID girdin.")
        return

    kayit = id_ile_kayit_bul(veriler, kayit_id)
    if not kayit:
        print("Bu ID ile kayit bulunamadi.")
        return

    print("\nBos biraktigin alanlar eski haliyle kalir.\n")

    yeni_model = input(f"Model adi [{kayit['model_adi']}]: ").strip()
    yeni_kategori = input(f"Kategori [{kayit['kategori']}]: ").strip()
    yeni_filament = input(f"Filament turu [{kayit['filament_turu']}]: ").strip().upper()
    yeni_renk = input(f"Renk [{kayit['renk']}]: ").strip()
    yeni_gram = input(f"Gram [{kayit['gram']}]: ").strip()
    yeni_sure = input(f"Sure [{kayit['sure']}]: ").strip()
    yeni_durum = input(f"Durum [{kayit['durum']}]: ").strip()
    yeni_not = input(f"Not [{kayit['not']}]: ").strip()

    if yeni_model:
        kayit["model_adi"] = yeni_model.title()

    if yeni_kategori:
        kayit["kategori"] = yeni_kategori.title()

    if yeni_filament:
        if yeni_filament in ["PLA", "ABS", "PETG"]:
            kayit["filament_turu"] = yeni_filament
        else:
            print("Gecersiz filament turu girildigi icin eski deger korundu.")

    if yeni_renk:
        kayit["renk"] = yeni_renk.title()

    if yeni_gram:
        try:
            gram_degeri = float(yeni_gram.replace(",", "."))
            if gram_degeri >= 0:
                kayit["gram"] = gram_degeri
            else:
                print("Gram negatif olamaz. Eski deger korundu.")
        except ValueError:
            print("Gram degeri gecersiz oldugu icin eski deger korundu.")

    if yeni_sure:
        try:
            sure_degeri = float(yeni_sure.replace(",", "."))
            if sure_degeri >= 0:
                kayit["sure"] = sure_degeri
            else:
                print("Sure negatif olamaz. Eski deger korundu.")
        except ValueError:
            print("Sure degeri gecersiz oldugu icin eski deger korundu.")

    if yeni_durum:
        if yeni_durum.lower() in ["hazirlaniyor", "basiliyor", "tamamlandi"]:
            kayit["durum"] = yeni_durum.title()
        else:
            print("Durum gecersiz oldugu icin eski deger korundu.")

    if yeni_not:
        kayit["not"] = yeni_not

    kayit["maliyet"] = maliyet_hesapla(kayit["gram"], kayit["filament_turu"])

    verileri_kaydet(veriler)
    print("\nKayit guncellendi.")
    print(f"Yeni hesaplanan maliyet: {kayit['maliyet']} TL")


def proje_sil():
    veriler = verileri_yukle()
    baslik_yaz()
    alt_baslik_yaz("PROJE SIL")

    if not veriler:
        print("Silinecek kayit bulunmuyor.")
        return

    try:
        kayit_id = int(input("Silinecek proje ID: "))
    except ValueError:
        print("Gecersiz ID girdin.")
        return

    kayit = id_ile_kayit_bul(veriler, kayit_id)
    if not kayit:
        print("Bu ID ile kayit bulunamadi.")
        return

    kayit_yazdir(kayit)
    onay = input("\nBu kaydi silmek istedigine emin misin? (E/H): ").strip().lower()

    if onay == "e":
        veriler.remove(kayit)
        verileri_kaydet(veriler)
        print("Kayit silindi.")
    else:
        print("Silme islemi iptal edildi.")