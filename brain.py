import random

def cevap_ver(mesaj):
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
