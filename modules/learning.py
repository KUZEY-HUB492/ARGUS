import json
import os

DOSYA = "data/learned.json"


def verileri_oku():
    if not os.path.exists(DOSYA):
        with open(DOSYA, "w", encoding="utf-8") as f:
            json.dump({}, f)

    with open(DOSYA, "r", encoding="utf-8") as f:
        return json.load(f)


def verileri_yaz(veriler):
    with open(DOSYA, "w", encoding="utf-8") as f:
        json.dump(veriler, f, ensure_ascii=False, indent=4)


def komut_ogret(kisa, gercek):
    veriler = verileri_oku()
    veriler[kisa] = gercek
    verileri_yaz(veriler)


def komut_getir(kisa):
    veriler = verileri_oku()
    return veriler.get(kisa)
def komut_sil(kisa):
    veriler = verileri_oku()

    if kisa in veriler:
        del veriler[kisa]
        verileri_yaz(veriler)
        return True

    return False


def komutlari_listele():
    return verileri_oku()