print("YENI COMMANDS.PY CALISTI")
import random
from datetime import datetime
from config import AI_NAME, VERSION
from modules.learning import (
    komut_ogret,
    komut_getir,
    komut_sil,
    komutlari_listele
)
from modules.memory import hafizaya_yaz, hafizadan_oku
from modules.system import sistem_bilgisi
from modules.modes import mod_calistir
from modules.web import site_ac
from modules.apps import uygulama_ac, uygulama_kapat
from datetime import datetime
import random
from datetime import datetime

print("YENI COMMANDS.PY CALISTI")

def komut_calistir(komut):
    def komut_temizle(k):
        k = k.lower()

        gereksizler = [
            "bana",
            "lütfen",
            "şunu",
            "bir",
            "tane"
        ]

        for kelime in gereksizler:
            k = k.replace(kelime, "")

        k = k.replace("'i", "")
        k = k.replace("yi", "")

        return k.strip()

    komut = komut_temizle(komut)

    # Öğrendiklerini göster komutu
    if komut == "öğrendiklerini göster":
        veriler = komutlari_listele()

        if not veriler:
            return "Henüz hiçbir komut öğrenmedim."

        cevap = "Öğrendiğim komutlar:\n"

        for kisa, gercek in veriler.items():
            cevap += f"• {kisa} → {gercek}\n"

        return cevap

    # Öğrenilmiş komut var mı?
    ogrenilen = komut_getir(komut)

    if ogrenilen:
        return ogrenilen

    # Öğrenme sistemi
    if komut.startswith("unut:"):
        kisa = komut.replace("unut:", "").strip()

        if komut_sil(kisa):
            return f'"{kisa}" komutunu unuttum efendim.'

        return "Böyle bir komut bilmiyorum."

    if komut.startswith("öğren:"):
        veri = komut.replace("öğren:", "").strip()

        if "=" not in veri:
            return "Kullanım: öğren: kısa komut = gerçek komut"

        kisa, gercek = veri.split("=", 1)

        komut_ogret(kisa.strip(), gercek.strip())

        return f'"{kisa.strip()}" komutunu öğrendim efendim.'

    

    if komut == "yardım":
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
            "- hafıza sistemi\n"
            "- web sitesi aç\n"
            "- öğren: kısa komut = gerçek komut\n"
        )
    if komut == "versiyon":
        return (
            f"{AI_NAME} {VERSION}\n\n"
            "Advanced Response & Guidance Utility System\n"
            "Geliştirici: KUZEY-HUB492"
        )
    
    # Saat ve tarih
    if komut == "saat":
        return datetime.now().strftime("%H:%M:%S")

    if komut == "tarih":
        return datetime.now().strftime("%d.%m.%Y")

    # Sistem bilgisi
    if komut == "sistem bilgisi":
        return sistem_bilgisi()

    # Hafıza sistemi
    if "benim adım ne" in komut:
        isim = hafizadan_oku("isim")

        if isim:
            return f"Adınız {isim} efendim."

        return "Henüz isminizi bilmiyorum efendim."

    if "benim adım" in komut:
        isim = komut.replace("benim adım", "").strip()

        hafizaya_yaz("isim", isim)

        return f"Tamam efendim, {isim} ismini hatırlayacağım."

    # Web sitesi açma
    if komut.endswith(" sitesini aç"):
        site = komut.replace(" sitesini aç", "").strip()

        return site_ac(site)

    # Mod sistemi
    if komut.endswith(" modu"):
        mod = komut.replace(" modu", "").strip()

        cevap = mod_calistir(mod)

        if cevap:
            return cevap

    # Uygulama kapatma
    if any(kelime in komut for kelime in ["kapat", "sonlandır", "durdur"]):
        isim = komut.replace("kapat", "").strip()

        return uygulama_kapat(isim)

    # Uygulama / site açma
    if any(kelime in komut for kelime in ["aç", "başlat", "çalıştır"]):
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

    if komut in ["merhaba", "selam", "selamlar", "hey"]:
        cevaplar = [
            "Merhaba efendim. Size nasıl yardımcı olabilirim?",
            "Hoş geldiniz efendim.",
            "Tekrar merhaba efendim.",
            "Sizi görmek güzel efendim.",
            "Merhaba efendim. ARGUS hizmetinizde."
        ]

        return random.choice(cevaplar)
    if komut in ["teşekkürler", "teşekkür ederim", "sağ ol", "eyvallah"]:
        cevaplar = [
            "Rica ederim efendim.",
            "Her zaman efendim.",
            "Yardımcı olabildiysem ne mutlu bana.",
            "Görevim efendim.",
            "Ne demek efendim."
        ]

        return random.choice(cevaplar)
    if komut in ["nasılsın", "iyi misin"]:
        cevaplar = [
            "Gayet iyiyim efendim. Siz nasılsınız?",
            "Sistemlerim normal çalışıyor efendim.",
            "Her şey yolunda efendim.",
            "Hazırım efendim."
        ]

        return random.choice(cevaplar)

    return None