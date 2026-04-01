import json
import os

DOSYA_ADI = "baski_kayitlari.json"


def dosya_hazirla():
    if not os.path.exists(DOSYA_ADI):
        with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
            json.dump([], dosya, ensure_ascii=False, indent=4)


def verileri_yukle():
    dosya_hazirla()
    with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
        try:
            return json.load(dosya)
        except json.JSONDecodeError:
            return []


def verileri_kaydet(veriler):
    with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
        json.dump(veriler, dosya, ensure_ascii=False, indent=4)


def yeni_id_uret(veriler):
    if not veriler:
        return 1
    return max(kayit["id"] for kayit in veriler) + 1