from modules.memory import hafizaya_yaz, hafizadan_oku
from modules.system import sistem_bilgisi
from modules.modes import mod_calistir
from modules.web import site_ac
from modules.apps import uygulama_ac, uygulama_kapat
from datetime import datetime


def komut_calistir(komut):

    def komut_temizle(komut):
        komut = komut.lower()

        gereksizler = [
            "bana",
            "lütfen",
            "şunu",
            "bir",
            "tane"
        ]

        for kelime in gereksizler:
            komut = komut.replace(kelime, "")

        komut = komut.replace("'i", "")
        komut = komut.replace("yi", "")
        

        return komut.strip()

    komut = komut_temizle(komut)

    # Temel cevaplar
    if komut == "merhaba":
        return "Merhaba. Sana nasıl yardımcı olabilirim?"


    elif komut == "yardım":
        return (
            "Kullanabileceğin komutlar:\n"
            "- merhaba\n"
            "- yardım\n"
            "- saat\n"
            "- tarih\n"
            "- sistem bilgisi\n"
            "- oyun modu\n"
            "- yayın modu\n"
            "- geliştirme modu\n"
            "- uygulama aç\n"
            "- uygulama kapat\n"
            "- hafıza sistemi"
        )


    # Saat ve tarih
    elif komut == "saat":
        return datetime.now().strftime("%H:%M:%S")


    elif komut == "tarih":
        return datetime.now().strftime("%d.%m.%Y")


    # Sistem bilgisi
    elif komut == "sistem bilgisi":
        return sistem_bilgisi()


    # Hafıza sistemi
    elif "benim adım ne" in komut:
        isim = hafizadan_oku("isim")

        if isim:
            return f"Adınız {isim} efendim."

        return "Henüz isminizi bilmiyorum efendim."


    elif "benim adım" in komut:
        isim = komut.replace("benim adım", "").strip()

        hafizaya_yaz("isim", isim)

        return f"Tamam efendim, {isim} ismini hatırlayacağım."


    # Web sitesi açma
    elif komut.endswith(" sitesini aç"):
        site = komut.replace(" sitesini aç", "").strip()

        return site_ac(site)


    # Mod sistemi
    elif komut.endswith(" modu"):
        mod = komut.replace(" modu", "").strip()

        cevap = mod_calistir(mod)

        if cevap:
            return cevap


    # Uygulama kapatma
    elif any(kelime in komut for kelime in ["kapat", "sonlandır", "durdur"]):
        isim = komut.replace("kapat", "").strip()

        return uygulama_kapat(isim)


    # Uygulama / site açma
    elif any(kelime in komut for kelime in ["aç", "başlat", "çalıştır"]):
        isim = komut.replace("aç", "").strip()

        web_siteleri = [
            "youtube",
            "google",
            "chatgpt",
            "kick",
            "spotify",
            "github"
        ]

        if isim in web_siteleri:
            return site_ac(isim)

        return uygulama_ac(isim)


    return None