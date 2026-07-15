import random
from modules.apps import uygulama_ac


def argus_zeka(mesaj):
    mesaj = mesaj.lower()


    # Uygulama açma
    if "aç" in mesaj:
        uygulama = mesaj.replace("aç", "").strip()
        return uygulama_ac(uygulama)


    # Selamlaşma
    if mesaj == "jarvis":
        return random.choice([
            "Dinliyorum efendim.",
            "Buyurun efendim.",
            "Komutunuzu bekliyorum.",
            "Sizi dinliyorum."
        ])


    elif mesaj == "selam":
        return "Merhaba efendim."


    elif mesaj == "nasılsın":
        return "Sistemlerim normal çalışıyor efendim."


    else:
        return "Üzgünüm efendim, bu komutu henüz anlayamadım."
