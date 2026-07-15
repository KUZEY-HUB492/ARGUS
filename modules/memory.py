import json
import os


MEMORY_FILE = "memory.json"


def hafizaya_yaz(anahtar, deger):
    veri = {}

    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as dosya:
            veri = json.load(dosya)

    veri[anahtar] = deger

    with open(MEMORY_FILE, "w", encoding="utf-8") as dosya:
        json.dump(veri, dosya, ensure_ascii=False, indent=4)


def hafizadan_oku(anahtar):
    if not os.path.exists(MEMORY_FILE):
        return None

    with open(MEMORY_FILE, "r", encoding="utf-8") as dosya:
        veri = json.load(dosya)

    return veri.get(anahtar)