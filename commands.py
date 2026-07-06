import os

def komut_calistir(komut):

    komutlar = {
        "not defterini aç": ("start notepad", "Not Defteri açılıyor efendim."),
        "hesap makinesini aç": ("start calc", "Hesap Makinesi açılıyor efendim."),
        "paint aç": ("start mspaint", "Paint açılıyor efendim."),
        "dosya gezginini aç": ("start explorer", "Dosya Gezgini açılıyor efendim.")
    }

    if komut in komutlar:
        komut_satiri, mesaj = komutlar[komut]
        os.system(komut_satiri)
        return mesaj

    return None