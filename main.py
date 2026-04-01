from proje_modulu import (
    proje_ekle,
    projeleri_listele,
    proje_ara,
    proje_duzenle,
    proje_sil
)
from rapor_modulu import (
    istatistik_goster,
    yuksek_tuketim_goster,
    filament_analizi_goster
)

import os
import traceback


def temizle():
    os.system("cls" if os.name == "nt" else "clear")


def kutu_yaz(baslik, secenekler, genislik=42):
    print("+" + "-" * genislik + "+")
    print("|" + baslik.center(genislik) + "|")
    print("+" + "-" * genislik + "+")

    for secenek in secenekler:
        print("| " + secenek.ljust(genislik - 1) + "|")

    print("+" + "-" * genislik + "+")


def ana_menu_goster():
    temizle()
    kutu_yaz("3D BASKI ATOLYE SISTEMI", [
        "1- Proje islemleri",
        "2- Raporlama islemleri",
        "3- Cikis"
    ])


def proje_menu_goster():
    temizle()
    kutu_yaz("PROJE ISLEMLERI", [
        "1- Yeni proje ekle",
        "2- Projeleri listele",
        "3- Proje ara",
        "4- Proje duzenle",
        "5- Proje sil",
        "6- Ana menuye don"
    ])


def rapor_menu_goster():
    temizle()
    kutu_yaz("RAPORLAMA ISLEMLERI", [
        "1- Genel istatistikleri goster",
        "2- Yuksek tuketim raporu",
        "3- Filament analizi",
        "4- Ana menuye don"
    ])


def bekle():
    input("\nDevam etmek icin Enter'a bas...")


def guvenli_calistir(fonksiyon):
    try:
        temizle()
        fonksiyon()
    except Exception as hata:
        print("\nBir hata olustu:")
        print(str(hata))
        print("\nDetayli hata bilgisi:\n")
        traceback.print_exc()
    bekle()


def proje_islemleri_calistir():
    while True:
        proje_menu_goster()
        secim = input("Seciminizi giriniz: ").strip()

        if secim == "1":
            guvenli_calistir(proje_ekle)
        elif secim == "2":
            guvenli_calistir(projeleri_listele)
        elif secim == "3":
            guvenli_calistir(proje_ara)
        elif secim == "4":
            guvenli_calistir(proje_duzenle)
        elif secim == "5":
            guvenli_calistir(proje_sil)
        elif secim == "6":
            break
        else:
            print("\nHatali secim yaptin.")
            bekle()


def raporlama_islemleri_calistir():
    while True:
        rapor_menu_goster()
        secim = input("Seciminizi giriniz: ").strip()

        if secim == "1":
            guvenli_calistir(istatistik_goster)
        elif secim == "2":
            guvenli_calistir(yuksek_tuketim_goster)
        elif secim == "3":
            guvenli_calistir(filament_analizi_goster)
        elif secim == "4":
            break
        else:
            print("\nHatali secim yaptin.")
            bekle()


def main():
    while True:
        ana_menu_goster()
        secim = input("Seciminizi giriniz: ").strip()

        if secim == "1":
            proje_islemleri_calistir()
        elif secim == "2":
            raporlama_islemleri_calistir()
        elif secim == "3":
            print("\nProgram kapatiliyor...")
            break
        else:
            print("\nGecersiz secim.")
            bekle()


if __name__ == "__main__":
    try:
        main()
    except Exception as hata:
        print("\nProgram kritik bir hatayla durdu:")
        print(str(hata))
        print("\nDetayli hata bilgisi:\n")
        traceback.print_exc()
        input("\nCikmak icin Enter'a bas...")